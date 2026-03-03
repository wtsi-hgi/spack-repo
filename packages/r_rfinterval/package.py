# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfinterval(RPackage):
	"""Predictive Inference for Random Forests

	An integrated package for constructing random forest prediction intervals using a fast implementation package 'ranger'. This package can apply the following three methods described in Haozhe Zhang, Joshua Zimmerman, Dan Nettleton, and Daniel J. Nordman (2019) <doi:10.1080/00031305.2019.1585288>: the out-of-bag prediction interval, the split conformal method, and the quantile regression forest.
	"""
	
	homepage = "http://github.com/haozhestat/rfinterval"
	cran = "rfinterval" 

	version("1.0.0", md5="4cf78cb5ac189c1d6489cbc8be343cfe")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
