# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlmix(RPackage):
	"""Bayesian Analysis of Finite Mixtures of Plackett-Luce Models for
Partial Rankings/Orderings

	Fit finite mixtures of Plackett-Luce models for partial top rankings/orderings within the Bayesian framework. It provides MAP point estimates via EM algorithm and posterior MCMC simulations via Gibbs Sampling. It also fits MLE as a special case of the noninformative Bayesian analysis with vague priors. In addition to inferential techniques, the package assists other fundamental phases of a model-based analysis for partial rankings/orderings, by including functions for data manipulation, simulation, descriptive summary, model selection and goodness-of-fit evaluation. Main references on the methods are Mollica and Tardella (2017) <doi.org/10.1007/s11336-016-9530-0> and Mollica and Tardella (2014) <doi/10.1002/sim.6224>.
	"""
	
	cran = "PLMIX" 

	version("2.1.1", md5="9ef2a3f9b5c598146620a1feec7502c6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-ggmcmc@1.2:", type=("build", "run"))
	depends_on("r-coda@0.19.1:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-rcdd@1.2:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.2:", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-label-switching@1.6:", type=("build", "run"))
	depends_on("r-radarchart@0.3.1:", type=("build", "run"))
	depends_on("r-prefmod@0.8.34:", type=("build", "run"))
	depends_on("r-rankdist@1.1.3:", type=("build", "run"))
	depends_on("r-statrank@0.0.6:", type=("build", "run"))
	depends_on("r-pmr@1.2.5:", type=("build", "run"))
	depends_on("r-plackettluce@0.2.3:", type=("build", "run"))
