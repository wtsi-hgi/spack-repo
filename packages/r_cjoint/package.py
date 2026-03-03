# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCjoint(RPackage):
	"""AMCE Estimator for Conjoint Experiments

	An R implementation of the Average Marginal Component-specific
    Effects (AMCE) estimator presented in Hainmueller, J., Hopkins, D., and Yamamoto
    T. (2014) <DOI:10.1093/pan/mpt024> Causal Inference in Conjoint Analysis: Understanding Multi-Dimensional
    Choices via Stated Preference Experiments. Political Analysis 22(1):1-30.
	"""
	
	cran = "cjoint" 

	version("2.1.1", md5="845a1e6ed6251adc192ad4d6ec90b12d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
