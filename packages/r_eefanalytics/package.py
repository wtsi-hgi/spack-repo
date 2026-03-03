# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REefanalytics(RPackage):
	"""Robust Analytical Methods for Evaluating Educational
Interventions using Randomised Controlled Trials Designs

	Analysing data from evaluations of educational interventions using a randomised controlled trial design. Various analytical tools to perform sensitivity analysis using different methods are supported (e.g. frequentist models with bootstrapping and permutations options, Bayesian models). The included commands can be used for simple randomised trials, cluster randomised trials and multisite trials. The methods can also be used more widely beyond education trials. This package can be used to evaluate other intervention designs using Frequentist and Bayesian multilevel models.
	"""
	
	homepage = "https://github.com/germaine86/eefAnalytics"
	cran = "eefAnalytics" 

	version("1.1.1", md5="11a3d22b95ce1a10b20f1c69ec79f6a7")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
