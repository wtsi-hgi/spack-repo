# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import glob

class RLeafcutter(RPackage):
    """Leafcutter quantifies RNA splicing variation using short-read RNA-seq data. The core idea is to leverage spliced reads (reads that span an intron) to quantify (differential) intron usage across samples."""

    homepage = "https://davidaknowles.github.io/leafcutter/"
    url = "https://github.com/davidaknowles/leafcutter/archive/refs/tags/v0.2.7.tar.gz"

    version("0.2.7", sha256="0e70ebce6be4b25bfabc0d489cbefa92ddede80380b1bbf4ec3a84182d10d1bd")
    version("0.2.6", sha256="3d88eabd03446de65f4c774a2af08eec2ee8507e61c718cf494f74bbb5313aa8")
    version("0.2.5", sha256="c926825c2b723e8718be4c480133310ee6f416114d21761ae77cd7645d06710d")
    version("0.2.4", sha256="62c5b284b7ed6e9d88ffa96092a588ba4393bf3bb6baa6f0a265edd1fde6f882")
    version("0.2.3", sha256="4e8ef96682c833d848b712a532197a2b36319b36c00e6408859180d4cc30b5e5")
    version("0.2.2", sha256="15d6a217292b2a54a21dbef1a6b98e3d5f07fb60471d12f02e86494f53e03968")
    version("0.2", sha256="6db09f403e20dd1150f65ecfa87084da03c6034e62a0b05d54a34c33dc431a74")

    depends_on("r@4", type=("build", "run"))
    depends_on("r-rcpp@0.12.0:", type=("build", "run"))
    depends_on("r-rstan@2.18.1:", type=("build", "run"))
    depends_on("r-rstantools@2:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-domc", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-intervals", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-gtable", type=("build", "run"))
    depends_on("r-stanheaders@2.21", type=("build", "run"))
    depends_on("r-bh@1.66.0:", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.3.3.0:", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))

    def patch(self):
        remove("README.md")
        for item in glob.glob("leafcutter/*"):
            move(item, ".")

        filter_file("# CXX_STD = CXX11", "CXX_STD = CXX14", "src/Makevars", string=True)
        filter_file("evalWithTimeout", "withTimeout", "R/differential_splicing.R", string=True)
        filter_file("evalWithTimeout", "withTimeout", "NAMESPACE", string=True)

    def setup_build_environment(self, env):
        env.set("CPATH", self.spec["r-rcppparallel"].prefix + "/rlib/R/library/RcppParallel/include/")
