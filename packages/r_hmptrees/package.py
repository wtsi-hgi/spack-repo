# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmptrees(RPackage):
	"""Statistical Object Oriented Data Analysis of RDP-Based Taxonomic
Trees from Human Microbiome Data

	Tools to model, compare, and visualize populations of taxonomic tree objects.
	"""
	
	cran = "HMPTrees" 

	version("1.4", md5="fc3da9aabfd96360d61b1224036e240d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-hmp", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
