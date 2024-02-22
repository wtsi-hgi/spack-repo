# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZetasuite(RPackage):
	"""Analyze High-Dimensional High-Throughput Dataset and Quality
Control Single-Cell RNA-Seq

	The advent of genomic technologies has enabled the generation of two-dimensional or even multi-dimensional high-throughput data, e.g., monitoring multiple changes in gene expression in genome-wide siRNA screens across many different cell types (E Robert McDonald 3rd (2017) <doi: 10.1016/j.cell.2017.07.005> and Tsherniak A (2017) <doi: 10.1016/j.cell.2017.06.010>) or single cell transcriptomics under different experimental conditions. We found that simple computational methods based on a single statistical criterion is no longer adequate for analyzing such multi-dimensional data. We herein introduce 'ZetaSuite', a statistical package initially designed to score hits from two-dimensional RNAi screens.We also illustrate a unique utility of 'ZetaSuite' in analyzing single cell transcriptomics to differentiate rare cells from damaged ones (Vento-Tormo R (2018) <doi: 10.1038/s41586-018-0698-6>). In 'ZetaSuite', we  have the following steps: QC of input datasets, normalization using Z-transformation, Zeta score calculation and hits selection based on defined Screen Strength.
	"""
	
	cran = "ZetaSuite" 

	version("1.0.1", md5="d1f567e0ea056b18351cfb062f00d210")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
