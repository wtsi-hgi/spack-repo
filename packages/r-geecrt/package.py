# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeecrt(RPackage):
	"""Bias-Corrected GEE for Cluster Randomized Trials

	Population-averaged models have been increasingly used in the design and analysis of 
             cluster randomized trials (CRTs). To facilitate the applications of population-averaged 
             models in CRTs, the package implements the generalized estimating equations (GEE) and 
             matrix-adjusted estimating equations (MAEE) approaches to jointly estimate the marginal 
             mean models correlation models both for general CRTs and stepped wedge CRTs. Despite the 
             general GEE/MAEE approach, the package also implements a fast cluster-period GEE method by 
             Li et al. (2022) <doi:10.1093/biostatistics/kxaa056>
             specifically for stepped wedge CRTs with large and variable cluster-period sizes and gives 
             a simple and efficient estimating equations approach based on the cluster-period means to 
             estimate the intervention effects as well as correlation parameters. In addition, the package 
             also provides functions for generating correlated binary data with specific mean vector and 
             correlation matrix based on the multivariate probit method in Emrich and Piedmonte (1991) <doi:10.1080/00031305.1991.10475828> or 
             the conditional linear family method in Qaqish (2003) <doi:10.1093/biomet/90.2.455>. 
	"""
	
	cran = "geeCRT" 

	version("1.1.3", md5="301721cfbaa240976e5837db52e13bf1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
