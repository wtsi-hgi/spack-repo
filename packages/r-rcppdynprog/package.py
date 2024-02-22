# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppdynprog(RPackage):
	"""'Rcpp' Dynamic Programming

	Dynamic Programming implemented in 'Rcpp'.  Includes example partition and out of sample fitting applications.  Also supplies additional custom coders for the 'vtreat' package.
	"""
	
	homepage = "https://github.com/WinVector/RcppDynProg/"
	cran = "RcppDynProg" 

	version("0.2.1", md5="8f87fd71385d3553e401ac1e5f6a9e56")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
