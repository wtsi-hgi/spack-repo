# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenocdm(RPackage):
	"""Continuous Development Models for Incremental Time-Series
Analysis

	Using the Bayesian state-space approach, we developed a continuous development model to quantify dynamic incremental changes in the response variable. While the model was originally developed for daily changes in forest green-up, the model can be used to predict any similar process. The CDM can capture both timing and rate of nonlinear processes. Unlike statics methods, which aggregate variations into a single metric, our dynamic model tracks the changing impacts over time. The CDM accommodates nonlinear responses to variation in predictors, which changes throughout development. 
	"""
	
	cran = "phenoCDM" 

	version("0.1.3", md5="16a7d70d8a76e4369fa10c2fc96dbf2e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
