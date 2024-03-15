# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBanova(RPackage):
	"""Hierarchical Bayesian ANOVA Models

	It covers several Bayesian Analysis of Variance (BANOVA) models used in analysis of experimental designs in which both within- and between- subjects factors are manipulated. They can be applied to data that are common in the behavioral and social sciences. The package includes: Hierarchical Bayes ANOVA models with normal response, t response, Binomial (Bernoulli) response, Poisson response, ordered multinomial response and multinomial response variables. All models accommodate unobserved heterogeneity by including a normal distribution of the parameters across individuals. Outputs of the package include tables of sums of squares, effect sizes and p-values, and tables of predictions, which are easily interpretable for behavioral and social researchers. The floodlight analysis and mediation analysis based on these models are also provided. BANOVA uses 'Stan' and 'JAGS' as the computational platform. References: Dong and Wedel (2017) <doi:10.18637/jss.v081.i09>; Wedel and Dong (2020) <doi:10.1002/jcpy.1111>.
	"""
	
	cran = "BANOVA" 

	version("1.2.1", md5="89f3d7487c2c9a195507df0060226e7e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rjags@3.13:", type=("build", "run"))
	depends_on("r-runjags@1.2.1.0:", type=("build", "run"))
	depends_on("r-coda@0.16.1:", type=("build", "run"))
	depends_on("r-rstan@2.15.1:", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
