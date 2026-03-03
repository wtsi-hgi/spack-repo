# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMilag(RPackage):
	"""Calculates Microbial Lag Duration (on the Population Level) from
Provided Growth Curve Data

	Microbial growth is often measured by growth curves i.e. a table of population sizes and times of measurements. 
  This package allows to use such growth curve data to determine the duration of "microbial lag phase" i.e. the time needed for microbes to restart divisions.
  It implements the most commonly used methods to calculate the lag duration, these methods are discussed and described in Opalek et.al. 2022.
  Citation: "How to determine microbial lag phase duration?", M. Opalek, B. Smug, D. Wloch-Salamon (2022) <doi:10.1101/2022.11.16.516631>. 
	"""
	
	cran = "miLAG" 

	version("1.0.2", md5="c4a413b99c07927d0d3f89d9e840f014")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-testthat@3.1.8:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.2:", type=("build", "run"))
	depends_on("r-nlsmicrobio@0.0.3:", type=("build", "run"))
