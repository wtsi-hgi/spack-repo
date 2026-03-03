# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianmediationa(RPackage):
	"""Bayesian Mediation Analysis

	We perform general mediation analysis in the Bayesian setting using the methods described in Yu and Li (2022, ISBN:9780367365479). With the package, the mediation analysis can be performed on different types of outcomes (e.g., continuous, binary, categorical, or time-to-event), with default or user-defined priors and predictive models. The Bayesian estimates and credible sets of mediation effects are reported as analytic results.
	"""
	
	homepage = "https://cran.r-project.org/package=BayesianMediationA"
	cran = "BayesianMediationA" 

	version("1.0.1", md5="b751dcfdc6dc47749671bea15c599ff2")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
