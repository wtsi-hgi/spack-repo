# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzysim(RPackage):
	"""Fuzzy Similarity in Species Distributions

	Functions to compute fuzzy versions of species occurrence patterns based on presence-absence data (including inverse distance interpolation, trend surface analysis, and prevalence-independent favourability obtained from probability of presence), as well as pair-wise fuzzy similarity (based on fuzzy logic versions of commonly used similarity indices) among those occurrence patterns. Includes also functions for model consensus and comparison (overlap and fuzzy similarity, loss or gain), and for data preparation, such as obtaining unique abbreviations of species names, cleaning and gridding (thinning) point occurrence data onto raster maps, selecting absences under specified criteria, converting species lists (long format) to presence-absence tables (wide format), transposing part of a data frame, selecting relevant variables for models, assessing the false discovery rate, or analysing and dealing with multicollinearity. Initially described in Barbosa (2015) <doi:10.1111/2041-210X.12372>.
	"""
	
	homepage = "fuzzysim.r-forge.r-project.org"
	cran = "fuzzySim" 

	version("4.10.7", md5="630b819a77bb98da33a84ae3db5cfea9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-modeva@3.9:", type=("build", "run"))
