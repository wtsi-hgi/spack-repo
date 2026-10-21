# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Scar(CMakePackage):
    """High-performance router for single-cell ATAC-seq reads."""

    homepage = "https://github.com/davidebolo1993/scar"
    git = "https://github.com/davidebolo1993/scar.git"

    license("MIT")

    version("20260302", commit="d2a18b2cab07c935d7ac2b56e13acff8c89a3ca3")

    depends_on("cmake@3.14:", type="build")
    depends_on("htslib@1.20:")
    depends_on("zlib-api")
    depends_on("bzip2")
    depends_on("xz")

    def patch(self):
        """Use Spack's HTSlib instead of downloading a private build."""

        filter_file(
            "FetchContent_Declare(",
            "if(FALSE)\nFetchContent_Declare(",
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            "add_executable(scar",
            """endif()

find_path(HTSLIB_INCLUDE htslib/sam.h)
find_library(HTSLIB_LIB hts)
if(NOT HTSLIB_INCLUDE OR NOT HTSLIB_LIB)
  message(FATAL_ERROR "Could not locate HTSlib")
endif()

add_executable(scar""",
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            "target_link_directories(scar PRIVATE ${HTSLIB_INSTALL_DIR}/lib)",
            "",
            "CMakeLists.txt",
            string=True,
        )
        filter_file("    hts", "    ${HTSLIB_LIB}", "CMakeLists.txt", string=True)
        filter_file(
            "add_dependencies(scar htslib_build)",
            "install(TARGETS scar DESTINATION bin)",
            "CMakeLists.txt",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            with open("metadata.tsv", "w", encoding="utf-8") as metadata:
                metadata.write(
                    "barcode pool_id donor_id celltypes_LEV1 celltypes_LEV2 bamfile\n"
                    "AAACGAAAGACCACGA-1 pool1 donor_A B B_naive input.bam\n"
                )

            scar = Executable(join_path(self.prefix.bin, "scar"))
            scar("filter", "-i", "metadata.tsv", "-o", "filtered.tsv", "-m", "1")
            with open("filtered.tsv", "r", encoding="utf-8") as filtered:
                assert filtered.readline().startswith("barcode\tpool_id\tdonor_id")
