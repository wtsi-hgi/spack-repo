# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepreg(RPackage):
	"""Stepwise Regression Analysis

	The stepwise regression analysis is a statistical technique used to identify a subset of predictor variables essential for constructing predictive models. This package performs stepwise regression analysis across various regression models such as linear, logistic, Cox proportional hazards, Poisson, and gamma regression. It incorporates diverse stepwise regression algorithms like forward selection, backward elimination, and bidirectional elimination alongside the best subset method. Additionally, it offers a wide range of selection criteria, including Akaike Information Criterion (AIC), corrected AIC (AICc), Sawa Bayesian Information Criterion (BIC), Schwarz Bayesian Information Criterion (SBC), Significant Levels (SL), among others. Moreover, it facilitates the concurrent selection of multiple methods and criteria for variable selection. For user-friendly exploration and analysis, StepReg provides an intuitive R Shiny app.
	"""
	
	cran = "StepReg" 

	version("1.5.0", md5="c36b7a877e5b5dc7978db815098472a7")
	version("1.4.4", md5="8c7addbe6ab1eec8e69a955975fdb83b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarytools", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
