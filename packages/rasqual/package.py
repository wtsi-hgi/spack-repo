# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Rasqual(MakefilePackage):
    """Map QTLs using population and allele-specific sequencing signals."""

    homepage = "https://github.com/natsuhiko/rasqual"
    git = "https://github.com/natsuhiko/rasqual.git"

    version("20210424", commit="5aa553cf1b6501cf7ecd61a5efb34f7f20d354c6")

    depends_on("gsl", type=("build", "link"))
    depends_on("lapack", type=("build", "link"))
    depends_on("blas", type=("build", "link"))
    depends_on("zlib-api", type=("build", "link"))

    def patch(self):
        # Only the ``integer`` typedef and three LAPACK declarations are used
        # from CLAPACK. Declare those directly for standard LAPACK providers.
        for header in ("blaswrap", "f2c", "clapack"):
            filter_file("#include <{0}.h>".format(header), "", "src/util.h", string=True)
        filter_file(
            "#include <gsl/gsl_randist.h>",
            """#include <gsl/gsl_randist.h>
typedef int integer;
static inline double min(double a, double b) { return a < b ? a : b; }
extern void dsytrf_(
    char *, integer *, double *, integer *, integer *, double *, integer *, integer *
);
extern void dsytrs_(
    char *, integer *, integer *, double *, integer *, integer *, double *, integer *, integer *
);
extern void dsytri_(char *, integer *, double *, integer *, integer *, double *, integer *);""",
            "src/util.h",
            string=True,
        )

        # Make help(usage) command exit with 0
        filter_file(
            "if(argc==1){usage(); return -1;}",
            "if(argc==1){usage(); return 0;}",
            "src/main.c",
            string=True,
        )

    def build(self, spec, prefix):
        cflags = " ".join(
            [
                "-std=gnu99",
                "-fPIC",
                "-fcommon",
                "-O2",
                spec["gsl"].headers.cpp_flags,
                spec["zlib-api"].headers.cpp_flags,
            ]
        )
        ldflags = " ".join(
            [
                spec["gsl"].libs.ld_flags,
                spec["lapack"].libs.ld_flags,
                spec["blas"].libs.ld_flags,
                spec["zlib-api"].libs.ld_flags,
                "-lm",
                "-lpthread",
            ]
        )
        make(
            "-C",
            "src",
            "CC={0}".format(spack_cc),
            "CFLAGS={0}".format(cflags),
            "LDFLAGS={0}".format(ldflags),
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("src/rasqual", prefix.bin)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            rasqual = Executable(join_path(self.prefix.bin, "rasqual"))
            rasqual()
