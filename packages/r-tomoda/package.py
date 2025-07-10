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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tomoda_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tomoda/tomoda_1.12.0.tar.gz"]

	version("1.12.0", sha256="dae83627d4ed12c516c9797b85d0c332f4bc7d090467de8c34ea6985355bb152")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
