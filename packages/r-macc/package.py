# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacc(RPackage):
	"""Mediation Analysis of Causality under Confounding

	Performs causal mediation analysis under confounding or correlated errors. This package includes a single level mediation model, a two-level mediation model, and a three-level mediation model for data with hierarchical structures. Under the two/three-level mediation model, the correlation parameter is identifiable and is estimated based on a hierarchical-likelihood, a marginal-likelihood or a two-stage method. See Zhao, Y., & Luo, X. (2014), Estimating Mediation Effects under Correlated Errors with an Application to fMRI, <arXiv:1410.7217> for details.
	"""
	
	cran = "macc" 

	version("1.0.1", md5="9447a0eba4c2200c05ba4842c431b0d3")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
