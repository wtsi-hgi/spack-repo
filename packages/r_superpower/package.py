# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperpower(RPackage):
	"""Simulation-Based Power Analysis for Factorial Designs

	Functions to perform simulations of ANOVA designs of up to three factors. Calculates the observed power and average observed effect size for all main effects and interactions in the ANOVA, and all simple comparisons between conditions. Includes functions for analytic power calculations and additional helper functions that compute effect sizes for ANOVA designs, observed error rates in the simulations, and functions to plot power curves. Please see Lakens, D., & Caldwell, A. R. (2021). "Simulation-Based Power Analysis for Factorial Analysis of Variance Designs". <doi:10.1177/2515245920951503>.
	"""
	
	homepage = "https://aaroncaldwell.us/SuperpowerBook/"
	cran = "Superpower" 

	version("0.2.0", md5="a2743937bb5b561c230d62778e652434")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-afex", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
