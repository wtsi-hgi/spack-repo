# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisty(RPackage):
	"""Miscellaneous Functions 'T. Yanagida'

	Miscellaneous functions for (1) data management (e.g., grand-mean and group-mean centering, coding variables and reverse coding items, scale and cluster scores, reading and writing Excel and SPSS files), (2) descriptive statistics (e.g., frequency table, cross tabulation, effect size measures), (3) missing data (e.g., descriptive statistics for missing data, missing data pattern, Little's test of Missing Completely at Random, and auxiliary variable analysis), (4) multilevel data (e.g., multilevel descriptive statistics, within-group and between-group correlation matrix, multilevel confirmatory factor analysis, level-specific fit indices, cross-level measurement equivalence evaluation,  multilevel composite reliability, and multilevel R-squared measures), (5) item analysis (e.g., confirmatory factor analysis, coefficient alpha and omega, between-group and longitudinal measurement equivalence evaluation), and (6) statistical analysis (e.g., confidence intervals, collinearity and residual diagnostics, dominance analysis, between- and within-subject analysis of variance, latent class analysis, t-test, z-test, sample size determination).
	"""
	
	cran = "misty" 

	version("0.6.2", md5="a30c4fcbba7e5d3dbd26a17b7b15a90e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
