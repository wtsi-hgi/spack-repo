# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoringrules(RPackage):
	"""Scoring Rules for Parametric and Simulated Distribution
Forecasts

	Dictionary-like reference for computing scoring rules in a wide
    range of situations. Covers both parametric forecast distributions (such as
    mixtures of Gaussians) and distributions generated via simulation.
	"""
	
	homepage = "https://github.com/FK83/scoringRules"
	cran = "scoringRules" 

	version("1.1.1", md5="be9a9c10613e5ff981b72b32b8da30d9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
