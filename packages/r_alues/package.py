# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlues(RPackage):
	"""Agricultural Land Use Evaluation System

	Evaluates land suitability for different crops production. 
  The package is based on the Food and Agriculture Organization (FAO) and the 
  International Rice Research Institute (IRRI) methodology for land evaluation. 
  Development of ALUES is inspired by similar tool for land evaluation, Land Use 
  Suitability Evaluation Tool (LUSET). The package uses fuzzy logic approach to evaluate 
  land suitability of a particular area based on inputs such as rainfall, temperature, 
  topography, and soil properties. The membership functions used for fuzzy modeling are 
  the following: Triangular, Trapezoidal and Gaussian. The methods for computing the 
  overall suitability of a particular area are also included, and these are the Minimum, 
  Maximum and Average. Finally, ALUES is a highly optimized library with core algorithms 
  written in C++.
	"""
	
	homepage = "https://github.com/alstat/ALUES/"
	cran = "ALUES" 

	version("0.2.1", md5="12fb8e7c4d46c1af5e06d07576b10fc1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
