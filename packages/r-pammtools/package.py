# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPammtools(RPackage):
	"""Piece-Wise Exponential Additive Mixed Modeling Tools for
Survival Analysis

	The Piece-wise exponential (Additive Mixed) Model
    (PAMM; Bender and others (2018) <doi: 10.1177/1471082X17748083>) is a
    powerful model class for the analysis of survival (or time-to-event) data,
    based on Generalized Additive (Mixed) Models (GA(M)Ms). It offers intuitive specification and robust estimation of complex survival models with stratified baseline hazards, random effects, time-varying effects, time-dependent covariates and cumulative effects (Bender and others (2019)), as well as support for left-truncated, competing risks and recurrent events data.
    pammtools provides tidy workflow for survival analysis with PAMMs,
    including data simulation, transformation and other functions for data
    preprocessing and model post-processing as well as visualization.
	"""
	
	homepage = "https://adibender.github.io/pammtools/"
	cran = "pammtools" 

	version("0.5.93", md5="0d6a074e2b94b4681cd49cfed8587458")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-survival@2.39.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
