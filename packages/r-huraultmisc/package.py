# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuraultmisc(RPackage):
	"""Guillem Hurault Functions' Library

	Contains various functions for data analysis, notably helpers and diagnostics for Bayesian modelling using Stan.
	"""
	
	homepage = "https://github.com/ghurault/HuraultMisc"
	cran = "HuraultMisc" 

	version("1.1.1", md5="befa3ec8d482a370445e3407101420cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
