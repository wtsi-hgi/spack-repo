# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScam(RPackage):
	"""Shape Constrained Additive Models

	Generalized additive models under shape
        constraints on the component functions of the linear predictor.       
        Models can include multiple shape-constrained (univariate
        and bivariate) and unconstrained terms. Routines of the 
        package 'mgcv' are used to set up the model matrix, print, 
        and plot the results. Multiple smoothing parameter 
        estimation by the Generalized Cross Validation or similar.
        See Pya and Wood (2015) <doi:10.1007/s11222-013-9448-7> 
        for an overview. A broad selection of shape-constrained 
        smoothers, linear functionals of smooths with shape constraints,
        and Gaussian models with AR1 residuals. 
	"""
	
	cran = "scam" 

	version("1.2-16", md5="da181086ac6232b7c63f96663e95ad44")
	version("1.2-15", md5="18f6e32325a8325a62f18998808617a7")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mgcv@1.8.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
