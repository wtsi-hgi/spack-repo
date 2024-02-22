# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapgam(RPackage):
	"""Mapping Smoothed Effect Estimates from Individual-Level Data

	Contains functions for mapping odds ratios, hazard ratios, or other effect estimates using individual-level data such as case-control study data, using generalized additive models (GAMs) or Cox models for smoothing with a two-dimensional predictor (e.g., geolocation or exposure to chemical mixtures) while adjusting linearly for confounding variables, using methods described by Kelsall and Diggle (1998), Webster at al. (2006), and Bai et al. (2020).  Includes convenient functions for mapping point estimates and confidence intervals, efficient control sampling, and permutation tests for the null hypothesis that the two-dimensional predictor is not associated with the outcome variable (adjusting for confounders).     
	"""
	
	cran = "MapGAM" 

	version("1.3", md5="f6faa2b295e28aaebcaa57bd1d720659")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-pbsmapping", type=("build", "run"))
