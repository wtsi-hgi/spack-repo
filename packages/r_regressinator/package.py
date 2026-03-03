# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegressinator(RPackage):
	"""Simulate and Diagnose (Generalized) Linear Models

	Simulate samples from populations with known covariate
    distributions, generate response variables according to common linear and
    generalized linear model families, draw from sampling distributions of
    regression estimates, and perform visual inference on diagnostics from model
    fits.
	"""
	
	homepage = "https://www.refsmmat.com/regressinator/"
	cran = "regressinator" 

	version("0.1.3", md5="39e60929a430464dec62cf9328f08124")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-nullabor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
