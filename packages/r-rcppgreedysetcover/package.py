# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppgreedysetcover(RPackage):
	"""Greedy Set Cover

	A fast implementation of the greedy algorithm for the set cover problem using 'Rcpp'.
	"""
	
	homepage = "http://github.com/matthiaskaeding/RcppGreedySetCover"
	cran = "RcppGreedySetCover" 

	version("0.1.0", md5="a2b7dbaf01d72c0729deaa867b61edb3")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp@0.12.14:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
