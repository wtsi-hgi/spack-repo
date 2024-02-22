# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpdensity(RPackage):
	"""Local Polynomial Density Estimation and Inference

	Without imposing stringent distributional assumptions or shape restrictions, nonparametric estimation has been popular in economics and other social sciences for counterfactual analysis, program evaluation, and policy recommendations. This package implements a novel density (and derivatives) estimator based on local polynomial regressions, documented in Cattaneo, Jansson and Ma (2022) <doi:10.18637/jss.v101.i02>: lpdensity() to construct local polynomial based density (and derivatives) estimator, and lpbwdensity() to perform data-driven bandwidth selection. 
	"""
	
	cran = "lpdensity" 

	version("2.4", md5="6e8735f0a182cf26ed01101cff2acfae")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
