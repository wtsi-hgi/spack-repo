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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CCPlotR_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CCPlotR/CCPlotR_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="577e586adf51f7b6265b9fc877880ed0749a9c9d15ac7bd2c4800b10941a69b0")

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
