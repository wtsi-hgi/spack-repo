# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecr(RPackage):
	"""Conducting and Visualizing Specification Curve Analyses

	Provides utilities for conducting specification curve analyses (Simonsohn, Simmons & Nelson (2020, <doi: 10.1038/s41562-020-0912-z>) or multiverse analyses (Steegen, Tuerlinckx, Gelman & Vanpaemel, 2016, <doi: 10.1177/1745691616658637>) including functions to setup, run, evaluate, and plot all specifications.
	"""
	
	homepage = "https://masurp.github.io/specr/"
	cran = "specr" 

	version("1.0.0", md5="25e7b37be2f2dd941a6c8811203e8575")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
