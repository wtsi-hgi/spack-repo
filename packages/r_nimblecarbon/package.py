# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimblecarbon(RPackage):
	"""Bayesian Analyses of Radiocarbon Dates with NIMBLE

	Provides utility functions and custom probability distribution for Bayesian analyses of radiocarbon dates within the 'nimble' modelling framework.  It includes various population growth models, nimbleFunction objects, as well as a suite of functions for prior and posterior predictive checks for demographic inference (Crema and Shoda (2021) <doi:10.1371/journal.pone.0251695>) and other analyses.
	"""
	
	cran = "nimbleCarbon" 

	version("0.2.5", md5="25f06614d7d51c5c375e9b9f57d22c0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nimble@0.12:", type=("build", "run"))
	depends_on("r-rcarbon", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
