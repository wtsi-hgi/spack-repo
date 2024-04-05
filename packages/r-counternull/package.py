# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounternull(RPackage):
	"""Randomization-Based Inference

	Randomization-Based Inference for customized experiments.
  Computes Fisher-Exact P-Values alongside null randomization 
  distributions. Retrieves counternull sets and generates counternull 
  distributions. Computes Fisher Intervals and Fisher-Adjusted P-Values. 
  Package includes visualization of randomization distributions and Fisher 
  Intervals. Users can input custom test statistics and their own methods for 
  randomization. 
  Rosenthal and Rubin (1994) <doi:10.1111/j.1467-9280.1994.tb00281.x>.
	"""
	
	homepage = "https://github.com/ymabene/Counternull"
	cran = "Counternull" 

	version("0.2.12", md5="32dfbce972d81d07b99fd9f65275a8c2")
	version("0.2.1", md5="000a9bfcd51b394c159ef90802f8ea8c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-randomizr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
