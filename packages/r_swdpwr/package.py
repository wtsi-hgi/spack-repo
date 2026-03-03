# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwdpwr(RPackage):
	"""Power Calculation for Stepped Wedge Cluster Randomized Trials

	To meet the needs of statistical power calculation for stepped wedge cluster randomized trials, we developed this software. Different parameters can be specified by users for different scenarios, including: cross-sectional and cohort designs, binary and continuous outcomes, marginal (GEE) and conditional models (mixed effects model), three link functions (identity, log, logit links), with and without time effects under exchangeable, nested exchangeable and block exchangeable correlation structures. Unequal numbers of clusters per sequence are also allowed. The methods included in this package: Zhou et al. (2020) <doi:10.1093/biostatistics/kxy031>, Li et al. (2018) <doi:10.1111/biom.12918>. Supplementary documents can be found at: <https://ysph.yale.edu/cmips/research/software/swdpwr/>. The Shiny app for swdpwr can be accessed at: <https://jiachenchen322.shinyapps.io/swdpwr_shinyapp/>. The package also includes functions that perform calculations for the intra-cluster correlation coefficients based on the random effects variances as input variables for continuous and binary outcomes, respectively. 
	"""
	
	cran = "swdpwr" 

	version("1.9", md5="24f36f39a994c4f90c77718d5cbb1463")

	depends_on("r-spatstat-random", type=("build", "run"))
