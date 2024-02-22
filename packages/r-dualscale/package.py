# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDualscale(RPackage):
	"""Dual Scaling Analysis of Data

	Dual Scaling, developed by Professor Shizuhiko Nishisato (1994, ISBN: 0-9691785-3-6), is a fundamental technique in multivariate analysis used for data scaling and correspondence analysis. Its utility lies in its ability to represent multidimensional data in a lower-dimensional space, making it easier to visualize and understand underlying patterns in complex data. This technique has been implemented to handle various types of data, including Contingency and Frequency data (CF), Multiple-Choice data (MC), Sorting data (SO), Paired-Comparison data (PC), and Rank-Order data (RO), providing users with a powerful tool to explore relationships between variables and observations in various fields, from sociology to ecology, enabling deeper and more efficient analysis of multivariate datasets.
	"""
	
	cran = "dualScale" 

	version("1.0.0", md5="85671e2625393d28b3100a7bfdc2ae50")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-eba", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
