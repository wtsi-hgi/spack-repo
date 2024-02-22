# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAugsimex(RPackage):
	"""Analysis of Data with Mixed Measurement Error and
Misclassification in Covariates

	Implementation of the augmented
            Simulation-Extrapolation (SIMEX) algorithm proposed by Yi et al. (2015) <doi:10.1080/01621459.2014.922777>
            for analyzing the data with mixed measurement error and misclassification. The main
            function provides a similar summary output as that of glm() function. Both parametric and
            empirical SIMEX are considered in the package.
	"""
	
	cran = "augSIMEX" 

	version("3.7.4", md5="2155b598adaa9a8e161e1a788e62ad4b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
