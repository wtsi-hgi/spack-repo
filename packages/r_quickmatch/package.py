# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickmatch(RPackage):
	"""Quick Generalized Full Matching

	
    Provides functions for constructing near-optimal generalized full matching.
    Generalized full matching is an extension of the original full matching method
    to situations with more intricate study designs. The package is made with
    large data sets in mind and derives matches more than an order of magnitude
    quicker than other methods.
	"""
	
	homepage = "https://github.com/fsavje/quickmatch"
	cran = "quickmatch" 

	version("0.2.2", md5="c36d99c6bcd45f13db50a0a1135b35d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-scclust@0.2:", type=("build", "run"))
