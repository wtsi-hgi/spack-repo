# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplmm(RPackage):
	"""Simultaneous Penalized Linear Mixed Effects Models

	Contains functions that fit linear mixed-effects models
        for high-dimensional data (p>>n) with penalty for both the fixed effects and random effects for variable selection. 
        The details of the algorithm can be found in Luoying Yang PhD thesis (Yang and Wu 2020). The algorithm implementation
        is based on the R package 'lmmlasso'. 
        Reference: Yang L, Wu TT (2020). Model-Based Clustering of Longitudinal Data in High-Dimensionality. Unpublished thesis.
	"""
	
	cran = "splmm" 

	version("1.1.3", md5="08c93376fee0955ff3fd5bef28b6360a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-emulator", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
