# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemicomprisks(RPackage):
	"""Hierarchical Models for Parametric and Semi-Parametric Analyses
of Semi-Competing Risks Data

	Hierarchical multistate models are considered to perform the analysis of independent/clustered semi-competing risks data. The package allows to choose the specification for model components from a range of options giving users substantial flexibility, including: accelerated failure time or proportional hazards regression models; parametric or non-parametric specifications for baseline survival functions and cluster-specific random effects distribution; a Markov or semi-Markov specification for terminal event following non-terminal event. While estimation is mainly performed within the Bayesian paradigm, the package also provides the maximum likelihood estimation approach for several parametric models. The package also includes functions for univariate survival analysis as complementary analysis tools.
	"""
	
	cran = "SemiCompRisks" 

	version("3.4", md5="82da834fd31e233259b86bb7c5a80dc4")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r@3.3:", type=("build", "run"))
