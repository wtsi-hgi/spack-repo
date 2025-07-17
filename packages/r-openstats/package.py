# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenstats(RPackage):
    """A Robust and Scalable Software Package for Reproducible Analysis of High-Throughput genotype-phenotype association

    Package contains several methods for statistical analysis of genotype to phenotype association in high-throughput screening pipelines.
    """

    homepage = "https://git.io/Jv5w0"
    bioc = "OpenStats"

    version("1.20.0", commit="7b82fcf8180fc870df373a6a848f0b4a2e071d5f")
    version("1.14.0", commit="3c449fc8bd425bf77b1d770bc93c50e92d15df07")

    depends_on("r-nlme", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-aiccmodavg", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-rlist", type=("build", "run"))
    depends_on("r-summarytools", type=("build", "run"))
