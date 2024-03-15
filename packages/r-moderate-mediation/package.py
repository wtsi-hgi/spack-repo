# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModerateMediation(RPackage):
	"""Causal Moderated Mediation Analysis

	Causal moderated mediation analysis using the methods proposed by Qin and Wang (2023) <doi:10.3758/s13428-023-02095-4>. Causal moderated mediation analysis is crucial for investigating how, for whom, and where a treatment is effective by assessing the heterogeneity of mediation mechanism across individuals and contexts. This package enables researchers to estimate and test the conditional and moderated mediation effects, assess their sensitivity to unmeasured pre-treatment confounding, and visualize the results. The package is built based on the quasi-Bayesian Monte Carlo method, because it has relatively better performance at small sample sizes, and its running speed is the fastest. The package is applicable to a treatment of any scale, a binary or continuous mediator, a binary or continuous outcome, and one or more moderators of any scale. 
	"""
	
	cran = "moderate.mediation" 

	version("0.0.8", md5="e0a6f815bb1f692eb8ab0fc7c3c888c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
