# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHorseshoenlm(RPackage):
	"""Nonlinear Regression using Horseshoe Prior

	Provides the posterior estimates of the regression coefficients when horseshoe prior is specified. 
             The regression models considered here are logistic model for binary response and 
             log normal accelerated failure time model for right censored survival response. 
             The linear model analysis is also available for completeness. 
             All models provide deviance information criterion and widely applicable information criterion. 
             See <doi:10.1111/rssc.12377> Maity et. al. (2019) <doi:10.1111/biom.13132> Maity et. al. (2020).  
	"""
	
	cran = "horseshoenlm" 

	version("0.0.6", md5="e56cc054aabae1a4bc6da15bd04a9c15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
