# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeanshiftr(RPackage):
	"""A Computationally Efficient Mean Shift Implementation

	Performs mean shift classification using linear and 
  k-d tree based nearest neighbor implementations for the Gaussian,
  Epanechnikov, and biweight product kernels. 
	"""
	
	homepage = "http://meanmean.me/meanshift/r/cran/2016/08/28/meanShiftR.html"
	cran = "meanShiftR" 

	version("0.56", md5="6f90398ca00e1e51b876d8fb50a5f082")

	depends_on("r@3.1:", type=("build", "run"))
