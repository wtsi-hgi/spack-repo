# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Ccmpred(CMakePackage):
    """CCMpred is a C implementation of a Markov Random Field pseudo-likelihood maximization for learning protein residue-residue contacts as made popular by Ekeberg et al. [1] and Balakrishnan and Kamisetty [2]. While predicting contacts with comparable accuracy to the referenced methods, however, CCMpred is written in C / CUDA C, performance-tuned and therefore much faster."""

    homepage = "https://github.com/soedinglab/CCMpred"
    git = "https://github.com/soedinglab/CCMpred.git"

    version("0.3.2", tag="v0.3.2", submodules=True)

    #depends_on("cuda", type=("build", "link"))
    depends_on("py-numpy", type="run")
    depends_on("py-biopython", type="run")
    depends_on("jansson", type=("build", "link", "run"))
    depends_on("ncurses", type=("build", "link", "run"))

    def patch(self):
        filter_file("#define fsqrt sqrtf", "", "lib/libconjugrad/include/conjugrad.h", string=True)
        filter_file("char* msgpackfilename = NULL;", "", "src/ccmpred.c", string=True)
        filter_file("optList = parseopt(argc, argv, optstr);", "optList = parseopt(argc, argv, optstr);char* msgpackfilename = NULL;", "src/ccmpred.c", string=True)
#        filter_file("add_definitions(-DCUDA)", "add_definitions(-DCUDA)\n	set_directory_properties( PROPERTIES COMPILE_DEFINITIONS \"\" )", "CMakeLists.txt", string=True)

#    def cmake_args(self):
#        return [
#            "-DGPU_ARCH=native",
#            "-DCMAKE_VERBOSE_MAKEFILE=ON"
#        ]

    def setup_build_environment(self, env):
        env.set("LDFLAGS", "-Wl,--copy-dt-needed-entries")
