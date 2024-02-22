# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcpa(RPackage):
	"""Behavioral Change Point Analysis of Animal Movement

	The Behavioral Change Point Analysis (BCPA) is a method of
    identifying hidden shifts in the underlying parameters of a time series,
    developed specifically to be applied to animal movement data which is
    irregularly sampled.  The method is based on: E. Gurarie, R. Andrews and 
    K. Laidre A novel method for identifying behavioural changes in animal 
    movement data (2009) Ecology Letters 12:5 395-408. A development version is 
    on <https://github.com/EliGurarie/bcpa>. NOTE: the BCPA method may be useful 
    for any univariate, irregularly sampled Gaussian time-series, but animal 
    movement analysts are encouraged to apply correlated velocity change point 
    analysis as implemented in the smoove package, as of this writing on GitHub 
    at <https://github.com/EliGurarie/smoove>. An example of a univariate analysis
    is provided in the UnivariateBCPA vignette. 
	"""
	
	cran = "bcpa" 

	version("1.3.2", md5="e0fc748d9eb55f67cc4e2ff46aca9b71")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
