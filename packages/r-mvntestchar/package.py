# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvntestchar(RPackage):
	"""Test for Multivariate Normal Distribution Based on a
Characterization

	Provides a test of multivariate normality of an unknown sample 
    that does not require estimation of the nuisance parameters, the mean and covariance 
    matrix.  Rather, a sequence of transformations removes these nuisance parameters and
    results in a set of sample matrices that are positive definite.  These matrices are 
    uniformly distributed on the space of positive definite matrices in the unit 
    hyper-rectangle if and only if the original data is multivariate normal (Fairweather,
    1973, Doctoral dissertation, University of Washington). The package performs a 
    goodness of fit test of this hypothesis. In addition to the test, functions in the 
    package give visualizations of the support region of positive definite matrices for 
    bivariate samples.
	"""
	
	cran = "MVNtestchar" 

	version("1.1.3", md5="d29f4d94c747b6389471bb23a70dd1d8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
