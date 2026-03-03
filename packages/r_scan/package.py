# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScan(RPackage):
	"""Single-Case Data Analyses for Single and Multiple Baseline
Designs

	A collection of procedures for analysing, visualising, 
  and managing single-case data. These include piecewise linear regression 
  models, multilevel models, overlap indices ('PND', 'PEM', 'PAND', 'PET', 'tau-u', 
  'baseline corrected tau', 'CDC'), and randomization tests. Data preparation functions 
  support outlier detection, handling missing values, scaling, truncation, 
  rank transformation, and smoothing. An export function helps to generate 
  html and latex tables in a publication friendly style. More details can be 
  found in the online book 'Analyzing single-case data with R and scan', Juergen Wilbert (2023)
  <https://jazznbass.github.io/scan-Book/>.
	"""
	
	homepage = "https://github.com/jazznbass/scan/"
	cran = "scan" 

	version("0.60.0", md5="71dae40c5843014ff07da8bee2b7ee49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-mblm", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
