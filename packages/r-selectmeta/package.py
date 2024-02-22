# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectmeta(RPackage):
	"""Estimation of Weight Functions in Meta Analysis

	Publication bias, the fact that studies identified for inclusion in a meta analysis do not represent all studies on the topic of interest, is commonly recognized as a threat to the validity of the results of a meta analysis. One way to explicitly model publication bias is via selection models or weighted probability distributions. In this package we provide implementations of several parametric and nonparametric weight functions. The novelty in Rufibach (2011) is the proposal of a non-increasing variant of the nonparametric weight function of Dear & Begg (1992). The new approach potentially offers more insight in the selection process than other methods, but is more flexible than parametric approaches. To maximize the log-likelihood function proposed by Dear & Begg (1992) under a monotonicity constraint we use a differential evolution algorithm proposed by Ardia et al (2010a, b) and implemented in Mullen et al (2009). In addition, we offer a method to compute a confidence interval for the overall effect size theta, adjusted for selection bias as well as a function that computes the simulation-based p-value to assess the null hypothesis of no selection as described in Rufibach (2011, Section 6).
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "selectMeta" 

	version("1.0.8", md5="92754f695d403c3df760edb941d0babb")

	depends_on("r-deoptim@2.0.6:", type=("build", "run"))
