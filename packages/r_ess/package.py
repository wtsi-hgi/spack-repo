# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REss(RPackage):
	"""Efficient Stepwise Selection in Decomposable Models

	An implementation of the ESS algorithm following Amol Deshpande, Minos Garofalakis,
	     Michael I Jordan (2013) <arXiv:1301.2267>. The ESS algorithm
	     is used for model selection in decomposable graphical models.
	"""
	
	homepage = "https://github.com/mlindsk/ess"
	cran = "ess" 

	version("1.1.2", md5="2e29165e31fe7f5b3e8c8cb5c60cae0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
