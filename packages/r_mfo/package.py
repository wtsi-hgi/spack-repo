# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfo(RPackage):
	"""Maximal Fat Oxidation and Kinetics Calculation

	Calculate the maximal fat oxidation, the exercise intensity that elicits the 
              maximal fat oxidation and the SIN model to represent the fat oxidation kinetics. 
              Three variables can be obtained from the SIN model: dilatation, symmetry and translation. 
              Examples of these methods can be found in Montes de Oca et al (2021) <doi:10.1080/17461391.2020.1788650>
              and Chenevière et al. (2009) <doi:10.1249/MSS.0b013e31819e2f91>.
	"""
	
	homepage = "https://github.com/JorgeDelro/MFO"
	cran = "MFO" 

	version("0.1.0", md5="6a7f92304ecb9d27b2bf69f39892b7be")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
