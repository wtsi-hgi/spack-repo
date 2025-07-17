# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcplotr(RPackage):
    """Plots For Visualising Cell-Cell Interactions

    CCPlotR is an R package for visualising results from tools that predict cell-cell interactions from single-cell RNA-seq data. These plots are generic and can be used to visualise results from multiple tools such as Liana, CellPhoneDB, NATMI etc.
    """

    homepage = "https://github.com/Sarah145/CCPlotR"
    bioc = "CCPlotR"

    version("1.6.0", commit="8bba4eed5600da2296144bf47f18732cc7725928")
    version("1.0.0", commit="560c3ded0b099dc5c62afbab5859c503f9a96cab")

    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-ggraph", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-scatterpie", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-ggbump", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-ggtext", type=("build", "run"))
    depends_on("r-ggh4x", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"))
