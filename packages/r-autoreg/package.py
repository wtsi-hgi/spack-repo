# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoreg(RPackage):
	"""Automatic Linear and Logistic Regression and Survival Analysis

	Make summary tables for descriptive statistics and select explanatory variables 
    automatically in various regression models. Support linear models, generalized linear 
    models and cox-proportional hazard models. Generate publication-ready tables summarizing 
    result of regression analysis and plots. The tables and plots can be exported in "HTML", 
    "pdf('LaTex')", "docx('MS Word')" and "pptx('MS Powerpoint')" documents.
	"""
	
	homepage = "https://github.com/cardiomoon/autoReg"
	cran = "autoReg" 

	version("0.3.3", md5="23c5865fc467c96eeee00238d7941ff4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-moonbook@0.3:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tidycmprsk", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-maxstat", type=("build", "run"))
	depends_on("r-pammtools", type=("build", "run"))
