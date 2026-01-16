# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ceo(CMakePackage):
    """Combinatorial Entropy Optimization toolkit with a C++ clustering
    backend and Python analysis script."""

    homepage = "https://github.com/sanderlab/ceo"
    git = "https://github.com/sanderlab/ceo.git"

    license("Proprietary")

    version("20250804", commit="6382003d788f557922c842eaae25525278244520")

    root_cmakelists_dir = "src"

    depends_on("cmake@3.16:", type="build")
    depends_on("eigen@3.3:")
    depends_on("fmt@8:")
    depends_on("cnpy")
    depends_on("boost+program_options")
    depends_on("zlib-api")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))

    def patch(self):
        """Drop the Conan-specific build flow and rely on Spack dependencies."""

        filter_file(
            r"^include\(\${CMAKE_BINARY_DIR}/conanbuildinfo\.cmake\)\s*\n",
            "",
            "src/CMakeLists.txt",
        )
        filter_file(r"^conan_basic_setup\(\)\s*\n", "", "src/CMakeLists.txt")
        filter_file(
            r"project\(ceo-clustering\)",
            """project(ceo-clustering)

find_package(Eigen3 REQUIRED)
find_package(fmt REQUIRED)
find_package(ZLIB REQUIRED)
find_package(Boost REQUIRED COMPONENTS program_options)

find_path(CNPY_INCLUDE_DIR cnpy.h)
find_library(CNPY_LIBRARY cnpy)
if (NOT CNPY_INCLUDE_DIR OR NOT CNPY_LIBRARY)
    message(FATAL_ERROR "Could not locate cnpy headers/libraries")
endif()

""",
            "src/CMakeLists.txt",
        )

        filter_file(
            r'add_definitions\("-std=c\+\+17"\)',
            """set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
""",
            "src/CMakeLists.txt",
        )

        filter_file(
            r"add_executable\(ceo-clustering main\.cpp ceo\.cpp\)",
            """add_executable(ceo-clustering main.cpp ceo.cpp)
target_include_directories(ceo-clustering PRIVATE ${CNPY_INCLUDE_DIR})
""",
            "src/CMakeLists.txt",
        )

        filter_file(
            r"target_link_libraries\(ceo-clustering \${CONAN_LIBS}\)",
            "target_link_libraries(ceo-clustering PRIVATE fmt::fmt ${CNPY_LIBRARY} Eigen3::Eigen ZLIB::ZLIB Boost::program_options)",
            "src/CMakeLists.txt",
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with working_dir(self.build_directory):
            install("ceo-clustering", prefix.bin)

        mkdirp(prefix.libexec)
        install(join_path(self.stage.source_path, "ceo.py"), prefix.libexec)

        wrapper = join_path(prefix.bin, "ceo")
        python = spec["python"].command.path
        with open(wrapper, "w", encoding="utf-8") as fout:
            fout.write("#! /bin/bash\n")
            fout.write(f'exec "{python}" "{join_path(prefix.libexec, "ceo.py")}" "$@"\n')

        set_executable(wrapper)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "ceo-clustering"))("--help")
