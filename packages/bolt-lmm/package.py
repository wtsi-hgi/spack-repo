# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class BoltLmm(MakefilePackage):
    """The BOLT-LMM software package currently consists of two main algorithms, the BOLT-LMM algorithm for mixed model association testing, and the BOLT-REML algorithm for variance components analysis (i.e., partitioning of SNP-heritability and estimation of genetic correlations). """

    homepage = "http://www.hsph.harvard.edu/alkes-price/software/"
    url = "https://storage.googleapis.com/broad-alkesgroup-public/BOLT-LMM/downloads/BOLT-LMM_v2.4.1.tar.gz"

    version("2.4.1", sha256="65f13a51277a0834e03911a9e98c9325be95d1d896a3e7b8d2aa759776a78aa6")

    depends_on("boost+program_options+iostreams", type=("build", "link"))
    depends_on("nlopt+cxx")
    depends_on("intel-oneapi-mkl")
    depends_on("zlib", type=("build", "link"))
    depends_on("zstd", type=("build", "link"))
    depends_on("glibc", type=("build", "link", "run"))
    depends_on("gcc", type=("build", "link"))

    def patch(self):
        filter_file("BOOST_INSTALL_DIR = /home/pl88/boost_1_58_0/install", "BOOST_INSTALL_DIR = " + self.spec["boost"].prefix, "src/Makefile", string=True)
        filter_file("NLOPT_INSTALL_DIR = /n/groups/price/poru/HSPH_SVN/src/BOLT-LMM/nlopt-2.4.2", "", "src/Makefile", string=True)
        filter_file("INTELROOT = /n/groups/price/poru/external_software/intel_mkl_2019u4", "INTELROOT = " + self.spec["intel-oneapi-mkl"].prefix, "src/Makefile", string=True)
        filter_file("ZLIB_STATIC_DIR = /n/groups/price/poru/external_software/zlib/zlib-1.2.11", "ZLIB_STATIC_DIR = " + self.spec["zlib"].prefix.include, "src/Makefile", string=True)
        filter_file("LIBSTDCXX_STATIC_DIR = /n/groups/price/poru/external_software/libstdc++/usr/lib/gcc/x86_64-redhat-linux/4.8.5/", "LIBSTDCXX_STATIC_DIR = " + self.spec["gcc"].prefix.lib64, "src/Makefile", string=True)
        filter_file("GLIBC_STATIC_DIR = /home/pl88/glibc-static/usr/lib64", "GLIBC_STATIC_DIR = " + self.spec["glibc"].prefix.lib, "src/Makefile", string=True)
        filter_file("ZSTD_DIR = /n/data1/bwh/medicine/loh/ploh/external_software/zstd-1.5.2/lib", "ZSTD_DIR = " + self.spec["zstd"].prefix.lib, "src/Makefile", string=True)
        filter_file("CC = icpc", "CC = g++", "src/Makefile", string=True)

        filter_file("-llapack", "-lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lm", "src/Makefile", string=True)

    def setup_build_environment(self, env):
        env.set("CPLUS_INCLUDE_PATH", self.spec["zlib"].prefix.include + ":" + self.spec["zstd"].prefix.include + ":" + self.spec["nlopt"].prefix.include)

    def build(self, spec, prefix):
        cd("src")
        make("bolt")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("bolt", prefix.bin)
