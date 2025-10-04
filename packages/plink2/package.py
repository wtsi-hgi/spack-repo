# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class Plink2(MakefilePackage):
    """PLINK2: Whole genome association analysis toolset, designed to perform a
    range of basic, large-scale analyses in a computationally efficient manner.

    This local recipe extends the builtin one to also install pgenlib headers
    and the static archive needed by dependents (e.g. SAIGE 1.5)."""

    homepage = "https://www.cog-genomics.org/plink/2.0/"
    url = "https://github.com/chrchang/plink-ng/archive/refs/tags/v2.00a5.11.tar.gz"
    list_url = "https://github.com/chrchang/plink-ng/tags"

    license("GPLv3")

    maintainers("wtsi-hgi")

    version(
        "2.0.0-a.6.9", sha256="492fc1e87b60b2209b7c3c1d616a01c1126978424cf795184d013ecf8a47e028"
    )
    version("2.00a5.11", sha256="8b664baa0b603f374123c32818ea2f053272840ba60e998d06cb864f3a6f1c38")
    version("2.00a5.10", sha256="53d845c6a04f8fc701e6f58f6431654e36cbf6b79bff25099862d169a8199a45")
    version("2.00a4.3", sha256="3cd1d26ac6dd1c451b42440f479789aa19d2b57642c118aac530a5ff1b0b4ce6")

    # libs
    depends_on("zlib-api")
    depends_on("zlib@1.2.12:", when="^[virtuals=zlib-api] zlib")
    depends_on("zstd@1.5.2:")
    depends_on("libdeflate@1.10:")
    depends_on("blas")
    depends_on("lapack")

    build_directory = "2.0/build_dynamic"

    def url_for_version(self, version):
        return f"https://github.com/chrchang/plink-ng/archive/refs/tags/v{version!s}.tar.gz"

    def edit(self, spec, prefix):
        with working_dir(self.build_directory):
            makefile = FileFilter("Makefile")
            if "avx2" in spec.target:
                makefile.filter(r"^NO_AVX2 = 1", "NO_AVX2 =")
            elif "sse4_2" in spec.target:
                makefile.filter(r"^NO_SSE42 = 1", "NO_SSE42 =")
            # ensure we statically include zstd objs for static libs
            makefile.filter(r"^STATIC_ZSTD =\s*$", "STATIC_ZSTD = 1")
            # use spack BLAS/LAPACK
            makefile.filter(
                r"^  BLASFLAGS=-llapack -lblas -lcblas -latlas",
                "  BLASFLAGS={0} {1}".format(
                    spec["blas"].libs.ld_flags, spec["lapack"].libs.ld_flags
                ),
            )
            # build position-independent code for static archives used in shared libs
            with open("Makefile", "a") as mf:
                mf.write("\n# Injected by Spack: ensure PIC for static libs used by dependents\n")
                mf.write("CFLAGS += -fPIC\n")
                mf.write("CXXFLAGS += -fPIC\n")
                mf.write("ZCFLAGS += -fPIC\n")
            # make plink2lib.a rule robust when STATIC_ZSTD is disabled
            makefile.filter(
                "\t$(CC) $(ZCFLAGS) $(ZCSRC2) $(ZSSRC2) -c",
                "\t$(SKIP_STATIC_ZSTD) $(CC) $(ZCFLAGS) $(ZCSRC2) $(ZSSRC2) -c",
                string=True,
            )

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            # build binaries and the pgenlib archive for dependents
            make()
            make("pgenlib.a")
            make("plink2lib.a")
            # additionally compile pvar_ffi_support into an object we can ship for dependents
            cxx = Executable(env.get('CXX', 'g++'))
            cxx("-std=c++11", "-O2", "-fPIC", "-I../include", "-I../libdeflate", "-I../../libdeflate", "-c", "../include/pvar_ffi_support.cc", "-o", "pvar_ffi_support.o")
            cxx("-std=c++11", "-O2", "-fPIC", "-I../include", "-I../libdeflate", "-I../../libdeflate", "-c", "../include/pgenlib_ffi_support.cc", "-o", "pgenlib_ffi_support.o")
            # archive it into plink2_includes.a for compatibility with SAIGE's expected name
            ar = which("ar")
            ar("rcs", "plink2_includes.a", "pvar_ffi_support.o", "pgenlib_ffi_support.o")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.lib)
        mkdir(prefix.include)
        with working_dir(self.build_directory):
            install("plink2", prefix.bin)
            install("pgen_compress", prefix.bin)
            # install the pgenlib static archive
            if os.path.exists("pgenlib.a"):
                install("pgenlib.a", prefix.lib)
            # install the plink2lib static archive with symbols used by dependents
            if os.path.exists("plink2lib.a"):
                install("plink2lib.a", prefix.lib)
            # install the compatibility archive expected by some dependents
            if os.path.exists("plink2_includes.a"):
                install("plink2_includes.a", prefix.lib)
        # headers for pgenlib and related includes
        install_tree(join_path(self.stage.source_path, "2.0", "include"), prefix.include)
