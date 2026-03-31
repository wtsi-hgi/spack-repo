import os

from spack.package import *


class Wfa2(CMakePackage):
    """Wavefront Alignment Algorithm library with C and C++ bindings."""

    homepage = "https://github.com/smarco/WFA2-lib"
    url = "https://github.com/smarco/WFA2-lib/archive/refs/tags/v2.3.6.tar.gz"
    git = "https://github.com/smarco/WFA2-lib.git"

    license("MIT")

    version("2.3.6", sha256="fd74c4bfdd5764ae8668cdeee7a80bfa35583b1980e261daa9dbf425bf12bb0b")

    depends_on("cmake@3.16:", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("gmake", type="build")

    @run_after("install")
    def install_test(self):
        test_src = r"""
#include <time.h>
extern "C" {
#include "wfa2lib/wavefront/wavefront_align.h"
}

int main() {
    wavefront_aligner_attr_t attr = wavefront_aligner_attr_default;
    wavefront_aligner_t* wf = wavefront_aligner_new(&attr);
    if (!wf) {
        return 1;
    }
    wavefront_aligner_delete(wf);
    return 0;
}
""".strip()
        cxx = Executable(self.compiler.cxx)
        with working_dir("spack-test", create=True):
            source = "smoke.cpp"
            with open(source, "w", encoding="utf-8") as f:
                f.write(test_src)
            exe = "test-wfa2"
            cxx(
                source,
                "-std=c++17",
                f"-I{self.prefix.include}",
                f"-I{join_path(self.prefix.include, 'wfa2lib')}",
                f"-L{self.prefix.lib}",
                "-lwfa2",
                "-lm",
                "-o",
                exe,
            )
            Executable(join_path(os.getcwd(), exe))()
