# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemicmprskcoxmsm(RPackage):
	"""Use Inverse Probability Weighting to Estimate Treatment Effect
for Semi Competing Risks Data

	Use inverse probability weighting methods to estimate treatment effect under marginal structure model (MSM) for the transition hazard of semi competing risk data, i.e. illness death model. We implement two specific such models, the usual Markov illness death structural model and the general Markov illness death structural model. We also provide the predicted three risks functions from the marginal structure models. Zhang, Y. and Xu, R. (2022) <arXiv:2204.10426>.
	"""
	
	cran = "semicmprskcoxmsm" 

	version("0.2.0", md5="ab941a19a345bc96e5a92b28eaf6e1cb")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
