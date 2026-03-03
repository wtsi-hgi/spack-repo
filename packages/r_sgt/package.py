# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgt(RPackage):
	"""Skewed Generalized T Distribution Tree

	Density, distribution function, quantile function and random generation for the skewed generalized t distribution. This package also provides a function that can fit data to the skewed generalized t distribution using maximum likelihood estimation.
	"""
	
	cran = "sgt" 

	version("2.0", md5="5a5c41d0d8d677bb42c0b1f3d73df23d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-optimx@2013.8.7:", type=("build", "run"))
	depends_on("r-numderiv@2014.2.1:", type=("build", "run"))
