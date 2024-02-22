# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQif(RPackage):
	"""Quadratic Inference Function

	Developed to perform the estimation and inference for regression 
    coefficient parameters in longitudinal marginal models using the method of 
    quadratic inference functions. Like generalized estimating equations, this 
    method is also a quasi-likelihood inference method. It has been showed that 
    the method gives consistent estimators of the regression coefficients even if 
    the correlation structure is misspecified, and it is more efficient than GEE 
    when the correlation structure is misspecified. Based on Qu, A., Lindsay, 
    B.G. and Li, B. (2000) <doi:10.1093/biomet/87.4.823>.
	"""
	
	cran = "qif" 

	version("1.5", md5="3f2ef54f11ef09a937cf1e394db0a8af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
