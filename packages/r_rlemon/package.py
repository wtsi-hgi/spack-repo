# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlemon(RPackage):
	"""R Access to LEMON Graph Algorithms

	Allows easy access to the LEMON Graph Library set of algorithms, written in C++.
             See the LEMON project page at <https://lemon.cs.elte.hu/trac/lemon>.
             Current LEMON version is 1.3.1.
	"""
	
	homepage = "https://errickson.net/rlemon/"
	cran = "rlemon" 

	version("0.2.1", md5="d06865da4f826cc8f77d5b0e8cae28d4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
