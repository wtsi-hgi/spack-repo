# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLa(RPackage):
	"""Lioness Algorithm (LA)

	Contains Lioness Algorithm (LA) for finding optimal designs over continuous design space, optimal Latin hypercube designs, and optimal order-of-addition designs. LA is a brand new nature-inspired meta-heuristic optimization algorithm. Detailed methodologies of LA and its implementation on numerical simulations can be found at Hongzhi Wang, Qian Xiao and Abhyuday Mandal (2021) <arXiv:2010.09154>.
	"""
	
	cran = "LA" 

	version("2.2", md5="3a6d35ece63000013790efff1ed8947d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
