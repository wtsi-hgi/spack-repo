# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Simde(MesonPackage):
    """The SIMDe header-only library provides fast, portable
    implementations of SIMD intrinsics on hardware which doesn't
    natively support them, such as calling SSE functions on ARM.
    There is no performance penalty if the hardware supports the
    native implementation (e.g., SSE/AVX runs at full speed on x86,
    NEON on ARM, etc.)."""

    homepage = "https://github.com/simd-everywhere/simde"
    url = "https://github.com/simd-everywhere/simde/archive/v0.6.0.tar.gz"
    git = "https://github.com/simd-everywhere/simde.git"

    license("MIT")

    version("0.7.6", sha256="c63e6c61392e324728da1c7e5de308cb31410908993a769594f5e21ff8de962b")
    version("0.7.2", sha256="366d5e9a342c30f1e40d1234656fb49af5ee35590aaf53b3c79b2afb906ed4c8")
    version("0.6.0", sha256="25a8b8c69c17ddc2f6209e86caa6b12d4ed91c0f841617efc56e5675eea84915")

    # depends_on("c", type="build")  # generated

    patch("sve-gcc.patch", when="@0.6.0 %gcc")
    conflicts("%gcc@8", when="target=a64fx", msg="Internal compiler error with gcc8 and a64fx")

    def meson_args(self):
        return ["-Dtests=false"]

    @run_after("install")
    def install_test(self):
        test_src = r"""
#include <simde/x86/sse2.h>

int main(void) {
    simde__m128i v = simde_mm_set_epi32(1, 2, 3, 4);
    simde__m128i w = simde_mm_add_epi32(v, v);
    return simde_mm_cvtsi128_si32(w) == 8 ? 0 : 1;
}
""".strip()
        cc = Executable(self.compiler.cc)
        with working_dir("spack-test", create=True):
            source = "simde-smoke.c"
            exe = "simde-smoke"
            with open(source, "w", encoding="utf-8") as f:
                f.write(test_src)
            cc(
                source,
                "-std=c99",
                f"-I{self.prefix.include}",
                "-o",
                exe,
            )
            Executable(join_path(os.getcwd(), exe))()
