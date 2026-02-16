# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Coordgen(CMakePackage):
    """Schrödinger, Inc's 2D coordinate generation"""

    homepage = "https://github.com/schrodinger/coordgenlibs"
    url = "https://github.com/schrodinger/coordgenlibs/archive/refs/tags/v3.0.2.tar.gz"

    maintainers("RMeli")

    license("BSD-3-Clause")

    version("3.0.2", sha256="f67697434f7fec03bca150a6d84ea0e8409f6ec49d5aab43badc5833098ff4e3")

    # depends_on("cxx", type="build")  # generated

    depends_on("maeparser")
    depends_on("boost")

    def patch(self):
        for needle in ("cmake_minimum_required(VERSION 2.8)", "cmake_minimum_required(VERSION 3.2)"):
            filter_file(
                needle,
                "cmake_minimum_required(VERSION 3.5)",
                "CMakeLists.txt",
                string=True,
            )

    def cmake_args(self):
        args = [
            "COORDGEN_USE_MAEPARSER",
            "COORDGEN_BUILD_SHARED_LIBS"
        ]
        return args
