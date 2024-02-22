# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernsmoothirt(RPackage):
	"""Nonparametric Item Response Theory

	Fits nonparametric item and option characteristic curves using kernel smoothing. It allows for optimal selection of the smoothing bandwidth using cross-validation and a variety of exploratory plotting tools. The kernel smoothing is based on methods described in Silverman, B.W. (1986). Density Estimation for Statistics and Data Analysis. Chapman & Hall, London.
	"""
	
	cran = "KernSmoothIRT" 

	version("6.4", md5="610a1e7dc557b3506a490482f2b006f3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
