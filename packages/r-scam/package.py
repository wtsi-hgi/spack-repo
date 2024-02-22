# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScam(RPackage):
	"""Shape Constrained Additive Models

	Routines for generalized additive modelling under shape
        constraints on the component functions of the linear predictor
        (Pya and Wood, 2015) <doi:10.1007/s11222-013-9448-7>.
        Models can contain multiple shape constrained (univariate
        and/or bivariate) and unconstrained terms. The routines of gam() 
        in package 'mgcv' are used for setting up the model matrix,  
        printing and plotting the results.  Penalized likelihood
        maximization based on Newton-Raphson method is used to fit a
        model with multiple smoothing parameter selection by GCV or
        UBRE/AIC.
	"""
	
	cran = "scam" 

	version("1.2-15", md5="18f6e32325a8325a62f18998808617a7")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mgcv@1.8.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
