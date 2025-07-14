# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTomoda(RPackage):
	"""Tomo-seq data analysis

	This package provides many easy-to-use methods to analyze and visualize tomo-seq data. The tomo-seq technique is based on cryosectioning of tissue and performing RNA-seq on consecutive sections. (Reference: Kruse F, Junker JP, van Oudenaarden A, Bakkers J. Tomo-seq: A method to obtain genome-wide expression data with spatial resolution. Methods Cell Biol. 2016;135:299-307. doi:10.1016/bs.mcb.2016.01.006) The main purpose of the package is to find zones with similar transcriptional profiles and spatially expressed genes in a tomo-seq sample. Several visulization functions are available to create easy-to-modify plots.
	"""
	
	homepage = "https://github.com/liuwd15/tomoda"
	bioc = "tomoda"

	version("1.18.0", commit="54eed164e11c23857ba0bc29d914e8abb486f0d3")
	version("1.12.0", commit="e35805a33ac2680e30b9f272ac06792ec98550b9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
