# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3mirt(RPackage):
	"""Descriptive 3D Multidimensional Item Response Theory Modeling

	For identifying, estimating, and plotting descriptive multidimensional item response theory models, restricted to 3D and dichotomous or polytomous data that fit the two-parameter logistic model or the graded response model. The method is foremost explorative and centered around the plot function that exposes item characteristics and constructs, represented by vector arrows, located in a three-dimensional interactive space. The results can be useful for item-level analysis as well as test development.
	"""
	
	homepage = "https://github.com/ForsbergPyschometrics/D3mirt"
	cran = "D3mirt" 

	version("1.1.0", md5="82d608f5895bcd7e15e9f720be8b0de0")

	depends_on("r-mirt", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rgl@1.0.1:", type=("build", "run"))
