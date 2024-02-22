# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarpCompo(RPackage):
	"""Network-Based Interpretation of Changes in Compositional Data

	Provides a set of functions to interpret changes in
 compositional data based on a network representation of all pairwise ratio
 comparisons: computation of all pairwise ratio, construction of a
 p-value matrix of all pairwise tests of these ratios between
 conditions, conversion of this matrix to a network.
	"""
	
	cran = "SARP.compo" 

	version("0.1.5", md5="1a1782aad86fe0b73b7e64a3456a20e2")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
