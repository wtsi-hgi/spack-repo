# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApctools(RPackage):
	"""Routines for Descriptive and Model-Based APC Analysis

	Age-Period-Cohort (APC) analyses are used to differentiate relevant drivers for long-term developments.
    The 'APCtools' package offers visualization techniques and general routines to simplify the workflow of an APC analysis.
    Sophisticated functions are available both for descriptive and regression model-based analyses.
    For the former, we use density (or ridgeline) matrices and (hexagonally binned) heatmaps as innovative visualization
    techniques building on the concept of Lexis diagrams.
    Model-based analyses build on the separation of the temporal dimensions based on generalized additive models,
    where a tensor product interaction surface (usually between age and period) is utilized
    to represent the third dimension (usually cohort) on its diagonal.
    Such tensor product surfaces can also be estimated while accounting for
    further covariates in the regression model.
    See Weigert et al. (2021) <doi:10.1177/1354816620987198> for methodological details.
	"""
	
	homepage = "https://bauer-alex.github.io/APCtools/"
	cran = "APCtools" 

	version("1.0.4", md5="a919bd2ebc83efe5e1712e6a0c610114")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
