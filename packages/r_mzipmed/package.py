# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMzipmed(RPackage):
	"""Mediation using MZIP Model

	We implement functions allowing for mediation analysis to be performed in cases where the mediator is a count variable with excess zeroes. First a function is provided allowing users to perform analysis for zero-inflated count variables using the marginalized zero-inflated Poisson (MZIP) model (Long et al. 2014 <DOI:10.1002/sim.6293>). Using the counterfactual approach to mediation and MZIP we can obtain natural direct and indirect effects for the overall population. Using delta method processes variance estimation can be performed instantaneously. Alternatively, bootstrap standard errors can be used. We also provide functions for cases with exposure-mediator interactions with four-way decomposition of total effect.
	"""
	
	cran = "mzipmed" 

	version("1.4.0", md5="e4a6bf04217711d66f993a5fccb6cc01")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
