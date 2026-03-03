# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRminqa(RPackage):
	"""Derivative-Free Optimization in R using C++

	Perform derivative-free optimization algorithms in R using C++.
    A wrapper interface is provided to call C function of the 'bobyqa' implementation
    (See <https://github.com/emmt/Algorithms/tree/master/bobyqa>).
	"""
	
	cran = "rminqa" 

	version("0.2.2", md5="9e32e49fec66b88f3bc5d026a45ab887")

	depends_on("r-rcpp", type=("build", "run"))
