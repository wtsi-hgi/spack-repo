# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Regenie(CMakePackage):
    """regenie is a C++ program for whole genome regression modelling of large genome-wide association studies."""

    homepage = "https://rgcgithub.github.io/regenie"
    url = "https://github.com/rgcgithub/regenie/archive/refs/tags/v3.3.tar.gz"

    version("3.3", sha256="ee5ccffa89c5ae37b4d89c367da0d0d47d808f1e157152d4d60bcbe1ab3e5f53")
    version("3.2.9", sha256="a268de7cd159fac5b94ac1da94d39a12bc922bf7b67f64a98172fc10511438a6")
    version("3.2.8", sha256="faeeec4b776743f3497b751bb7142e4c3a640fe69663a8ae56174859ed609822")
    version("3.2.7", sha256="bc3548bc04a011dfdbead80b5b1fae0be00d6fcc0e75c59326a50dfe2924c15a")
    version("3.2.6", sha256="da7115555c9db5477fa5a278bafaf5819062e1af67f08b6e8d49edb5b3c0f9b2")
    version("3.2.5.3", sha256="e34f722618c56ccf72b3f659c7e8c111683aec8dab67cd8f07985ee7e4c52284")
    version("3.2.5", sha256="4b9df5d6de77933947aabd3b66475bff7d51ee241db50194558a7349fe9e47b5")
    version("3.2.4", sha256="47a36bb6ae1ec79c9779a9276745a48c8336abaa08b71a9a8dc865818c8034cd")
    version("3.2.3", sha256="3e65874384eac157617be9bc6c3877160bfd3da44bba4c55ddaaa23ebdf08a37")
    version("3.2.2", sha256="04f22bdfdd0aa0f16c9b69c7baa7a571a8c196bc8699150fa888a5c7257ccbe8")

    depends_on("bgen")
    depends_on("boost+iostreams+system+filesystem")
    depends_on("intel-oneapi-mkl")
    depends_on("openblas")
    depends_on("openmpi")
    depends_on("sqlite")
    depends_on("zstd")
    depends_on("pkg-config")

    def patch(self):
        #filter_file("find_library(DB_LIBRARY libdb.a HINTS \"${BGEN_PATH}/build/db\" REQUIRED)", "", "CMakeLists.txt", string=True)
        #filter_file("find_library(Boost_LIBRARY libboost.a HINTS \"${BGEN_PATH}/build/3rd_party/boost_1_55_0\" REQUIRED)", "find_library(Boost_LIBRARY libboost_system.a libboost_iostreams.a HINTS \""+self.spec["boost"].prefix.lib+"\" REQUIRED)", "CMakeLists.txt", string=True)
        filter_file("find_library(Boost_LIBRARY libboost.a HINTS \"${BGEN_PATH}/build/3rd_party/boost_1_55_0\" REQUIRED)", "target_link_libraries(regenie PRIVATE -lboost_filesystem)", "CMakeLists.txt", string=True)
        filter_file("${Boost_LIBRARY}", self.spec["boost"].prefix.lib, "CMakeLists.txt", string=True)
        filter_file("target_include_directories(regenie PRIVATE ${BGEN_PATH} ${BGEN_PATH}/genfile/include/ ${BGEN_PATH}/3rd_party/boost_1_55_0/ ${BGEN_PATH}/3rd_party/zstd-1.1.0/lib ${BGEN_PATH}/db/include/ ${BGEN_PATH}/3rd_party/sqlite3)", "target_include_directories(regenie PRIVATE ${BGEN_PATH} ${BGEN_PATH}/genfile/include/ ${BGEN_PATH}/db/include/)", "CMakeLists.txt", string=True)

    def setup_build_environment(self, env):
        env.set("BGEN_PATH", self.spec["bgen"].prefix)
        env.set("OPENBLAS_ROOT", self.spec["openblas"].prefix.include)
        env.set("HAS_BOOST_IOSTREAM", "1")
        #env.set("LDFLAGS", "-lboost_system -lboost_filesystem -lmpi -lsqlite3 -lzstd")
