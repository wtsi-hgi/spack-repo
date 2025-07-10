# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnainteract(RPackage):
	"""Estimate Pairwise Interactions from multidimensional features

	RNAinteract estimates genetic interactions from multi-dimensional read-outs like features extracted from images. The screen is assumed to be performed in multi-well plates or similar designs. Starting from a list of features (e.g. cell number, area, fluorescence intensity) per well, genetic interactions are estimated. The packages provides functions for reporting interacting gene pairs, plotting heatmaps and double RNAi plots. An HTML report can be written for quality control and analysis.
	"""
	
	bioc = "RNAinteract" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNAinteract_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNAinteract/RNAinteract_1.50.0.tar.gz"]

	version("1.50.0", sha256="74d9aadb4a6cfbb7690bf7d5a895a4a5d28fea9521a6ac37d5a6af1e8e6ecd76")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ics", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-cellhts2", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-splots@1.13.12:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
