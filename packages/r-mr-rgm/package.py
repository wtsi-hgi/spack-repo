# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrRgm(RPackage):
	"""Multivariate Bidirectional Mendelian Randomization Networks

	Addressing a central challenge encountered in Mendelian randomization (MR) studies, where MR primarily focuses on discerning the effects of individual exposures on specific outcomes and establishes causal links between them. Using a network-based methodology, the intricacy involving interdependent outcomes due to numerous factors has been tackled through this routine. Based on Ni et al. (2018) <doi:10.1214/17-BA1087>, 'MR.RGM' extends to a broader exploration of the causal landscape by leveraging on network structures and involves the construction of causal graphs that capture interactions between response variables and consequently between responses and instrument variables. 'MR.RGM' facilitates the navigation of various data availability scenarios effectively by accommodating three input formats, i.e., individual-level data and two types of summary-level data. In the process, causal effects, adjacency matrices, and other essential parameters of the complex biological networks, are estimated. Besides, 'MR.RGM' provides uncertainty quantification for specific network structures among response variables.
	"""
	
	homepage = "https://github.com/bitansa/MR.RGM"
	cran = "MR.RGM" 

	version("0.0.2", md5="326875c82b6c6d7c95a7c91cb5d35288")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
