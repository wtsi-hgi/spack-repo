# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Chi2comb(CMakePackage):
    """C library computing CDFs of linear combinations of chi-square random variables."""

    homepage = "https://github.com/limix/chi2comb"
    url = "https://github.com/limix/chi2comb/archive/refs/tags/0.0.3.tar.gz"
    git = "https://github.com/limix/chi2comb.git"

    license("MIT")

    version("0.0.3", sha256="a727f68e6da9e6ca10226f0a9ce3efc70c09c806170e98cdb8578edf7d083135")

    depends_on("cmake@3.2:", type="build")

    @run_after("install")
    def install_test(self):
        """Build and run a tiny program that links against libchi2comb."""
        test_source = """\
#include <chi2comb.h>
#include <math.h>
int main(void) {
    struct chi2comb_chisquareds chi2s = {
        (double[2]){0.4, 1.1},
        (double[2]){1.3, 2.9},
        (int[2]){1, 3},
        2};
    struct chi2comb_info info;
    double result = 0.0;
    int err = chi2comb_cdf(2.0, &chi2s, 0.41, 1000, 1e-6, &info, &result);
    if (err != 0) {
        return err;
    }
    double tail = 1.0 - result;
    return fabs(tail - 0.9183206009070191) > 1e-6;
}
"""

        libs = find_libraries("libchi2comb", root=self.prefix, shared=True, recursive=True)
        cc = Executable(self.compiler.cc)

        with working_dir("spack-test", create=True):
            source = "chi2comb_test.c"
            with open(source, "w", encoding="utf-8") as f:
                f.write(test_source)

            cc(
                source,
                "-I{0}".format(self.prefix.include),
                *libs.ld_flags.split(),
                "-lm",
                "-o",
                "chi2comb-test",
            )

            Executable("./chi2comb-test")()
