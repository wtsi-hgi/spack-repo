# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCici(RPackage):
	"""Causal Inference with Continuous (Multiple Time Point)
Interventions

	Estimation of counterfactual outcomes for multiple values of continuous interventions at different time points, and plotting of causal dose-response curves. Details are given in Schomaker, McIlleron, Denti, Diaz (2023) <arXiv:2305.06645>.
	"""
	
	cran = "CICI" 

	version("0.9.1", md5="57959ec479e37ab69a2f92720271cff0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rngtools", type=("build", "run"))
