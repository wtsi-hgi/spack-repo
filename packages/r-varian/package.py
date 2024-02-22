# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarian(RPackage):
	"""Variability Analysis in R

	Uses a Bayesian model to
    estimate the variability in a repeated
    measure outcome and use that as an outcome or a predictor
    in a second stage model.
	"""
	
	homepage = "https://github.com/ElkhartGroup/varian"
	cran = "varian" 

	version("0.2.2", md5="2b83d301da0d4412ab8465bbacf6fb23")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rstan@2.7:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
