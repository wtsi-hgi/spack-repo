# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInext(RPackage):
	"""Interpolation and Extrapolation for Species Diversity

	Provides simple functions to compute and plot two types 
    (sample-size- and coverage-based) rarefaction and extrapolation curves for species
    diversity (Hill numbers) based on individual-based abundance data or sampling-unit-
    based incidence data; see Chao and others (2014, Ecological Monographs) for pertinent
    theory and methodologies, and Hsieh, Ma and Chao (2016, Methods in Ecology and Evolution)
    for an introduction of the R package.
	"""
	
	homepage = "http://chao.stat.nthu.edu.tw/wordpress/software_download/"
	cran = "iNEXT" 

	version("3.0.0", md5="2f15a5543bb602fba9882970a5ea12ee")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
