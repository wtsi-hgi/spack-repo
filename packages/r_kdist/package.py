# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdist(RPackage):
	"""K-Distribution and Weibull Paper

	Density, distribution function, quantile function and random generation
             for the K-distribution. A plotting function that plots data on Weibull
             paper and another function to draw additional lines. See results from package in T Lamont-Smith (2018), submitted J. R. Stat. Soc.
	"""
	
	cran = "kdist" 

	version("0.2", md5="0243ae69f9a9677d695eebab5ade9005")

	depends_on("r@3.1.1:", type=("build", "run"))
