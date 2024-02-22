# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcerisk(RPackage):
	"""Generalized Competing Event Model

	Generalized competing event model based on Cox PH model and Fine-Gray model.
    This function is designed to develop optimized risk-stratification methods for competing
    risks data, such as described in:
    1. Carmona R, Gulaya S, Murphy JD, Rose BS, Wu J, Noticewala S,McHale MT, Yashar CM, Vaida F,
    and Mell LK (2014) <DOI:10.1016/j.ijrobp.2014.03.047>.
    2. Carmona R, Zakeri K, Green G, Hwang L, Gulaya S, Xu B, Verma R, Williamson CW, Triplett DP, Rose
    BS, Shen H, Vaida F, Murphy JD, and Mell LK (2016) <DOI:10.1200/JCO.2015.65.0739>.
    3. Lunn, Mary, and Don McNeil (1995) <DOI:10.2307/2532940>.
	"""
	
	cran = "gcerisk" 

	version("19.05.24", md5="f4bf34c7cd00943632ec515d7acfc65b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
