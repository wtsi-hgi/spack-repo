# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgriutilities(RPackage):
	"""Utilities for Data Analysis in Agriculture

	Utilities designed to make the analysis of field trials easier and
 more accessible for everyone working in plant breeding. It provides a simple
 and intuitive interface for conducting single and multi-environmental trial
 analysis, with minimal coding required. Whether you're a beginner or an
 experienced user, 'agriutilities' will help you quickly and easily carry out
 complex analyses with confidence. With built-in functions for fitting Linear
 Mixed Models, 'agriutilities' is the ideal choice for anyone who wants to save
 time and focus on interpreting their results.
 Some of the functions require the R package 'asreml' for the 'ASReml' software,
 this can be obtained upon purchase from 'VSN' international (<https://vsni.co.uk/software/asreml-r>).
	"""
	
	homepage = "https://github.com/AparicioJohan/agriutilities"
	cran = "agriutilities" 

	version("1.2.0", md5="3130cbea86773a6f72856d46ca3630f8")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-statgensta", type=("build", "run"))
	depends_on("r-spats", type=("build", "run"))
