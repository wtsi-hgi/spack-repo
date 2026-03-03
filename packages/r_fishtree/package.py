# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishtree(RPackage):
	"""Interface to the Fish Tree of Life API

	An interface to the Fish Tree of Life API to download taxonomies,
    phylogenies, fossil calibrations, and diversification rate information for
    ray-finned fishes.
	"""
	
	homepage = "https://fishtreeoflife.org/"
	cran = "fishtree" 

	version("0.3.4", md5="3601b92ba3a801ea0ce560e6de2fe6e6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape@5.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang@0.4.1:", type=("build", "run"))
