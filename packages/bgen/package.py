# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Bgen(CMakePackage):
    """A BGEN file format reader."""

    homepage = "https://github.com/limix/bgen"
    url = "https://github.com/limix/bgen/archive/refs/tags/v4.1.9.tar.gz"

    version("4.1.9", sha256="4fbd0e35d072689fdc8b96d5ba1ea5838a0e5a30906cea72b6fa77f9c91ae92c")
    version("4.1.8", sha256="4241b56a0981803a3dd8aa3656ed466ef52d0058252888a175d14a87d344172e")
    version("4.1.7", sha256="5deaf0efae4022063720f62efecfbbf50eeea502da8440fe1e216a66b7c9d322")
    version("4.1.6", sha256="77b58c2df7eff69d5b8e8726e6fa7ddd95daca6df6635007919f32f46a25d27e")

    def cmake_args(self):
        return ["-DCMAKE_POSITION_INDEPENDENT_CODE=ON"]
