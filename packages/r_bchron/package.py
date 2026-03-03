# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBchron(RPackage):
	"""Radiocarbon Dating, Age-Depth Modelling, Relative Sea Level Rate
Estimation, and Non-Parametric Phase Modelling

	Enables quick calibration of radiocarbon dates under various 
  calibration curves (including user generated ones); age-depth modelling 
  as per the algorithm of Haslett and Parnell (2008) <DOI:10.1111/j.1467-9876.2008.00623.x>; Relative sea level 
  rate estimation incorporating time uncertainty in polynomial regression 
  models (Parnell and Gehrels 2015) <DOI:10.1002/9781118452547.ch32>; non-parametric phase modelling via 
  Gaussian mixtures as a means to determine the activity of a site 
  (and as an alternative to the Oxcal function SUM; currently 
  unpublished), and reverse calibration of dates from calibrated into 
  un-calibrated years (also unpublished).
	"""
	
	homepage = "https://andrewcparnell.github.io/Bchron/"
	cran = "Bchron" 

	version("4.7.6", md5="6515a7330340a91a1f870d136ba99b75")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
