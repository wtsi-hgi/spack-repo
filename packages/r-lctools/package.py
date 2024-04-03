# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLctools(RPackage):
	"""Local Correlation, Spatial Inequalities, Geographically Weighted
Regression and Other Tools

	Provides researchers and educators with easy-to-learn user friendly tools for calculating 
    key spatial statistics and to apply simple as well as advanced methods of spatial analysis in real data. 
    These include: Local Pearson and Geographically Weighted Pearson Correlation Coefficients, 
    Spatial Inequality Measures (Gini, Spatial Gini, LQ, Focal LQ), Spatial Autocorrelation 
    (Global and Local Moran's I), several Geographically Weighted Regression techniques and other 
    Spatial Analysis tools (other geographically weighted statistics). This package also contains functions for 
    measuring the significance of each statistic calculated, mainly based on Monte Carlo simulations.
	"""
	
	homepage = "https://stamatisgeoai.eu"
	cran = "lctools" 

	version("0.2-10", md5="4e33111bb4b134a35b05c223bafcbd19")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
