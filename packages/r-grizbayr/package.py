# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrizbayr(RPackage):
	"""Bayesian Inference for A|B and Bandit Marketing Tests

	Uses simple Bayesian conjugate prior update rules to calculate 
    the win probability of each option, value remaining in the test, and 
    percent lift over the baseline for various marketing objectives.
    References: 
    Fink, Daniel (1997) "A Compendium of Conjugate Priors" <https://www.johndcook.com/CompendiumOfConjugatePriors.pdf>.
    Stucchio, Chris (2015) "Bayesian A/B Testing at VWO" <https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf>.
	"""
	
	homepage = "https://github.com/rangi513/grizbayr"
	cran = "grizbayr" 

	version("1.3.5", md5="a3c92210423ffc0d475cf81200880ec8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
