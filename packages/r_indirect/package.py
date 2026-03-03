# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndirect(RPackage):
	"""Elicitation of Independent Conditional Means Priors for
Generalised Linear Models

	Functions are provided to facilitate prior elicitation for Bayesian generalised linear models using independent conditional means priors. The package supports the elicitation of multivariate normal priors for generalised linear models. The approach can be applied to indirect elicitation for a generalised linear model that is linear in the parameters. The package is designed such that the facilitator executes functions within the R console during the elicitation session to provide graphical and numerical feedback at each design point. Various methodologies for eliciting fractiles (equivalently, percentiles or quantiles) are supported, including versions of the approach of Hosack et al. (2017) <doi:10.1016/j.ress.2017.06.011>. For example, experts may be asked to provide central credible intervals that correspond to a certain probability. Or experts may be allowed to vary the probability allocated to the central credible interval for each design point. Additionally, a median may or may not be elicited. 
	"""
	
	cran = "indirect" 

	version("0.2.1", md5="e836c39cb4ac94dca398ed66b926d37f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
