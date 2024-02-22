# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltopt(RPackage):
	"""Optimal Experimental Designs for Accelerated Life Testing

	Creates the optimal (D, U and I) designs for the accelerated life
    testing with right censoring or interval censoring. It uses generalized 
    linear model (GLM) approach to derive the asymptotic variance-covariance 
    matrix of regression coefficients. The failure time distribution is assumed 
    to follow Weibull distribution with a known shape parameter and log-linear 
    link functions are used to model the relationship between failure time 
    parameters and stress variables. The acceleration model may have multiple 
    stress factors, although most ALTs involve only two or less stress factors. 
    ALTopt package also provides several plotting functions including contour plot,
    Fraction of Use Space (FUS) plot and Variance Dispersion graphs of Use Space
    (VDUS) plot. For more details, see Seo and Pan (2015) <doi:10.32614/RJ-2015-029>.
	"""
	
	cran = "ALTopt" 

	version("0.1.2", md5="18ed018d95eb607057b043a78213fcf0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cubature@1:", type=("build", "run"))
	depends_on("r-lattice@0.20:", type=("build", "run"))
