# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChngpt(RPackage):
	"""Estimation and Hypothesis Testing for Threshold Regression

	Threshold regression models are also called two-phase regression, broken-stick regression, split-point regression, structural change models, and regression kink models, with and without interaction terms. Methods for both continuous and discontinuous threshold models are included, but the support for the former is much greater. This package is described in Fong, Huang, Gilbert and Permar (2017) <DOI:10.1186/s12859-017-1863-x> and the package vignette.
	"""
	
	cran = "chngpt" 

	version("2023.11-29", md5="ff1f93784d95a1dfc036188440ed16bc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kyotil@2020.10.12:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
