# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexgam(RPackage):
	"""Generalized Additive Models with Flexible Response Functions

	Standard generalized additive models assume a response function, 
    which induces an assumption on the shape of the distribution of the 
    response. However, miss-specifying the response function results in biased 
    estimates. Therefore in Spiegel et al. (2017) 
    <doi:10.1007/s11222-017-9799-6> we propose to estimate the response function
    jointly with the covariate effects. This package provides the underlying 
    functions to estimate these generalized additive models with flexible 
    response functions. The estimation is based on an iterative algorithm. In 
    the outer loop the response function is estimated, while in the inner loop 
    the covariate effects are determined. For the response function a strictly
    monotone P-spline is used while the covariate effects are estimated based on
    a modified Fisher-Scoring algorithm. Overall the estimation relies on the 
    'mgcv'-package. 
	"""
	
	cran = "FlexGAM" 

	version("0.7.2", md5="b27cba79d5df3c0d46f7965811cc995d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv@1.8.23:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
