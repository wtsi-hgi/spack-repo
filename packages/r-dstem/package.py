# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDstem(RPackage):
	"""Multiple Testing of Local Extrema for Detection of Change Points

	Simultaneously detect the number and locations of change points in piecewise linear models under stationary Gaussian noise allowing autocorrelated random noise. The core idea is to transform the problem of detecting change points into the detection of local extrema (local maxima and local minima)through kernel smoothing and differentiation of the data sequence, see Cheng et al. (2020) <doi:10.1214/20-EJS1751>. A low-computational and fast algorithm call 'dSTEM' is introduced to detect change points based on the 'STEM' algorithm in D. Cheng and A. Schwartzman (2017) <doi:10.1214/16-AOS1458>.
	"""
	
	homepage = "https://doi.org/10.1214/20-EJS1751"
	cran = "dSTEM" 

	version("2.0-1", md5="3d556eed5d38adc2f13b2bece50e15b4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
