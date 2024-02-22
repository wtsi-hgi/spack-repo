# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobma(RPackage):
	"""Robust Bayesian Meta-Analyses

	A framework for estimating ensembles of meta-analytic models
    (assuming either presence or absence of the effect, heterogeneity, and
    publication bias). The RoBMA framework uses Bayesian model-averaging to 
    combine the competing meta-analytic models into a model ensemble, weights 
    the posterior parameter distributions based on posterior model probabilities 
    and uses Bayes factors to test for the presence or absence of the
    individual components (e.g., effect vs. no effect; Bartoš et al., 2022, 
    <doi:10.1002/jrsm.1594>; Maier, Bartoš & Wagenmakers, 2022, 
    <doi:10.1037/met0000405>). Users can define a wide range of non-informative 
    or informative prior distributions for the effect size, heterogeneity, 
    and publication bias components (including selection models and PET-PEESE). 
    The package provides convenient functions for summary, visualizations, and 
    fit diagnostics.
	"""
	
	homepage = "https://fbartos.github.io/RoBMA/"
	cran = "RoBMA" 

	version("3.1.0", md5="4ff3cd2fb86d512770fca4f9f2e92207")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bayestools@0.2.16:", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("jags@4.3.1:", type=("build", "link", "run"))
