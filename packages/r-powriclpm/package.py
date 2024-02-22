# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowriclpm(RPackage):
	"""Perform Power Analysis for the Random Intercept Cross-Lagged
Panel Model

	Perform user-friendly power analyses for the bivariate random
    intercept cross-lagged panel model (RI-CLPM). The strategy as proposed
    by Mulder (2022) <doi:10.1080/10705511.2022.2122467> is implemented.
    Extended power analysis options include the use of bounded estimation,
    inclusion of measurement error in the data generating model and
    estimation model (i.e., the stable trait autoregressive trait state,
    STARTS, model), imposing various constraints over time on the
    parameters of the estimation model, among others.
	"""
	
	homepage = "https://jeroendmulder.github.io/powRICLPM/"
	cran = "powRICLPM" 

	version("0.1.1", md5="ef9827236b2cea2115e68b5c1c12b278")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lavaan@0.6.7:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
