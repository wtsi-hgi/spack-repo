import os
import textwrap

from llnl.util.filesystem import mkdirp
from spack.package import *


class Tabixpp(MakefilePackage):
    """C++ wrapper around tabix providing libtabix and tabix++ binaries."""

    homepage = "https://github.com/vcflib/tabixpp"
    url = "https://github.com/vcflib/tabixpp/archive/refs/tags/v1.1.2.tar.gz"
    git = "https://github.com/vcflib/tabixpp.git"

    license("MIT")

    version("1.1.2", sha256="c850299c3c495221818a85c9205c60185c8ed9468d5ec2ed034470bb852229dc")

    depends_on("htslib")
    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("xz")
    depends_on("curl")

    def _make_args(self):
        hts = self.spec["htslib"]
        includes = f"-I{hts.prefix.include}"
        libpath = f"-L{hts.prefix.lib}"
        hts_headers = " ".join(
            [
                join_path(hts.prefix.include, "htslib", "bgzf.h"),
                join_path(hts.prefix.include, "htslib", "tbx.h"),
            ]
        )
        hts_lib = join_path(hts.prefix.lib, "libhts.a")
        return [
            f"INCLUDES={includes}",
            f"LIBPATH={libpath}",
            f"HTS_HEADERS={hts_headers}",
            f"HTS_LIB={hts_lib}",
        ]

    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        makefile.filter(r"LIB\s*=.*", "LIB = libtabixpp.a")
        makefile.filter(r"SLIB\s*=.*", "SLIB = libtabixpp.so.$(SOVERSION)")

    def build(self, spec, prefix):
        make(*self._make_args())

    def install(self, spec, prefix):
        make(
            "install",
            *self._make_args(),
            f"PREFIX={prefix}",
            "DESTDIR=",
        )
        with working_dir(prefix.lib):
            if os.path.exists("libtabixpp.so.1") and not os.path.exists("libtabixpp.so"):
                symlink("libtabixpp.so.1", "libtabixpp.so")
        pc_dir = join_path(prefix.lib, "pkgconfig")
        mkdirp(pc_dir)
        ldflags = [
            "-L{0}".format(prefix.lib),
            "-ltabixpp",
            self.spec["htslib"].libs.ld_flags,
            self.spec["zlib-api"].libs.ld_flags,
            self.spec["bzip2"].libs.ld_flags,
            self.spec["xz"].libs.ld_flags,
            self.spec["curl"].libs.ld_flags,
            "-lpthread",
            "-lm",
        ]
        pc_contents = textwrap.dedent(
            f"""\
            prefix={prefix}
            exec_prefix=${{prefix}}
            libdir=${{exec_prefix}}/lib
            includedir=${{prefix}}/include

            Name: tabixpp
            Description: C++ wrapper around tabix
            Version: {self.spec.version}
            Libs: {' '.join(ldflags)}
            Cflags: -I${{includedir}}
            """
        )
        with open(join_path(pc_dir, "tabixpp.pc"), "w", encoding="utf-8") as pcfile:
            pcfile.write(pc_contents)

    @run_after("install")
    def install_test(self):
        test_src = r"""
#include "tabix.hpp"

static_assert(sizeof(Tabix) > 0, "Tabix class must be available");

int main() {
    return 0;
}
""".strip()
        cxx = Executable(self.compiler.cxx)
        with working_dir("spack-test", create=True):
            source = "tabixpp-smoke.cpp"
            exe = "tabixpp-smoke"
            with open(source, "w", encoding="utf-8") as f:
                f.write(test_src)
            compile_args = [
                source,
                "-std=c++17",
                f"-I{self.prefix.include}",
                f"-I{self.spec['htslib'].prefix.include}",
                f"-L{self.prefix.lib}",
                "-ltabixpp",
            ]
            for dep in ("htslib", "zlib-api", "bzip2", "xz", "curl"):
                compile_args.extend(self.spec[dep].libs.ld_flags.split())
            compile_args.extend(["-lpthread", "-lm", "-o", exe])
            cxx(*compile_args)
            Executable(join_path(os.getcwd(), exe))()
