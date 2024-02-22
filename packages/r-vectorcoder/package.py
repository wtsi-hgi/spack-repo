# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVectorcoder(RPackage):
	"""Easily Analyze Your Gait Patterns Using Vector Coding Technique

	
  Facilitate the analysis of inter-limb and intra-limb coordination in human movement. 
  It provides functions for calculating the phase angle between two segments, enabling researchers and practitioners to quantify the coordination patterns within and between limbs during various motor tasks.
  Needham, R., Naemi, R., & Chockalingam, N. (2014) <doi:10.1016/j.jbiomech.2013.12.032>.
  Needham, R., Naemi, R., & Chockalingam, N. (2015) <doi:10.1016/j.jbiomech.2015.07.023>.
  Tepavac, D., & Field-Fote, E. C. (2001) <doi:10.1123/jab.17.3.259>.
  Park, J.H., Lee, H., Cho, Js. et al. (2021) <doi:10.1038/s41598-020-80237-w>.
	"""
	
	cran = "VectorCodeR" 

	version("0.2.0", md5="0eb0de9e35a2764acf14b776bca5ebb4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
