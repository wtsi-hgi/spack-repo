# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoicemodelr(RPackage):
	"""Choice Modeling in R

	Implements an MCMC algorithm to estimate a hierarchical multinomial logit model with a normal heterogeneity distribution. The algorithm uses a hybrid Gibbs Sampler with a random walk metropolis step for the MNL coefficients for each unit. Dependent variable may be discrete or continuous. Independent variables may be discrete or continuous with optional order constraints. Means of the distribution of heterogeneity can optionally be modeled as a linear function of unit characteristics variables.
	"""
	
	homepage = "https://www.decisionanalyst.com/"
	cran = "ChoiceModelR" 

	version("1.3.0", md5="8cab0e1cba4bbcfab18fc9017ba39a54")

	depends_on("r@3.5:", type=("build", "run"))
