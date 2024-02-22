# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLongcart(RPackage):
	"""Recursive Partitioning for Longitudinal Data and Right Censored
Data Using Baseline Covariates

	Constructs tree for continuous longitudinal data and survival data using baseline covariates as partitioning variables according to the 'LongCART' and 'SurvCART' algorithm, respectively. Later also included functions to calculate conditional power and predictive power of success based on interim results and probability of success for a prospective trial.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "LongCART" 

	version("3.2", md5="4fa48d4b4d5237959eb8b059f658c893")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
