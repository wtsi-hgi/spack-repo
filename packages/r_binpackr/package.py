# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinpackr(RPackage):
	"""Fast 1d Bin Packing

	Implements the First Fit Decreasing algorithm to achieve one dimensional heuristic bin packing. Runtime is of order O(n log(n)) where n is the number of items to pack. See "The Art of Computer Programming Vol. 1" by Donald E. Knuth (1997, ISBN: 0201896834) for more details.
	"""
	
	homepage = "https://github.com/lschneiderbauer/binpackr"
	cran = "binpackr" 

	version("0.1.1", md5="9a96381ba5e0059c1511c1361849bcb0")

	depends_on("r-cpp11", type=("build", "run"))
