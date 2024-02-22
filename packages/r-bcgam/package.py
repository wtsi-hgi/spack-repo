# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcgam(RPackage):
	"""Bayesian Constrained Generalised Linear Models

	Fits generalised partial linear regression models using a Bayesian approach, where shape and
			smoothness constraints are imposed on nonparametrically modelled predictors through shape-restricted splines, and 
			no constraints are imposed on optional parametrically modelled covariates. See Meyer et al. (2011) <doi/10.1080/10485252.2011.597852> 
			for more details. IMPORTANT: before installing 'bcgam', you need to install 'Rtools' (Windows) or 'Xcode' (Mac OS X). These are	
			required for the correct installation of 'nimble' (<https://r-nimble.org/download>). 			
	"""
	
	cran = "bcgam" 

	version("1.0", md5="806982c1b2f7354614fc4928f0125456")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-nimble@0.6.9:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
