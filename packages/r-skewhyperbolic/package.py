# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewhyperbolic(RPackage):
	"""The Skew Hyperbolic Student t-Distribution

	Functions are provided for the density function,
	     distribution function, quantiles and random number
	     generation for the skew hyperbolic
	     t-distribution. There are also functions that fit
	     the distribution to data. There are functions for the
	     mean, variance, skewness, kurtosis and mode of a given
	     distribution and to calculate moments of any order about
	     any centre. To assess goodness of fit, there are
	     functions to generate a Q-Q plot, a P-P plot and a tail plot.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/rmetrics/"
	cran = "SkewHyperbolic" 

	version("0.4-2", md5="347c31fb3dffede495c570773d3ac563")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-distributionutils", type=("build", "run"))
	depends_on("r-generalizedhyperbolic", type=("build", "run"))
