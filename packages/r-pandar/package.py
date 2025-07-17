# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPandar(RPackage):
    """PANDA Algorithm

    Runs PANDA, an algorithm for discovering novel network structure by combining information from multiple complementary data sources.
    """

    bioc = "pandaR"

    version("1.40.0", commit="76a2972f1e02a9f42baae8e1d1cc9878d546d653")
    version("1.34.0", commit="2c60e4285e02781819d80c85b399eda0647b05f8")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-runit", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
