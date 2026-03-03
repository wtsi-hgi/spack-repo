# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMertools(RPackage):
	"""Tools for Analyzing Mixed Effect Regression Models

	Provides methods for extracting results from mixed-effect model
    objects fit with the 'lme4' package. Allows construction of prediction intervals
    efficiently from large scale linear and generalized linear mixed-effects models.
    This method draws from the simulation framework used in the Gelman and Hill (2007) textbook:
    Data Analysis Using Regression and Multilevel/Hierarchical Models.
	"""
	
	cran = "merTools" 

	version("0.6.2", md5="f91777cba079e4940a040037db718f7f")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-lme4@1.1.11:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-blme", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
