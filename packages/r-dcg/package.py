# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcg(RPackage):
	"""Data Cloud Geometry (DCG): Using Random Walks to Find Community
Structure in Social Network Analysis

	Data cloud geometry (DCG) applies random walks in finding community structures for social networks. 
    Fushing, VanderWaal, McCowan, & Koehl (2013) (<doi:10.1371/journal.pone.0056259>).
	"""
	
	cran = "DCG" 

	version("0.9.3", md5="4365eb01eb7780e8ce2d2ba414a5f477")

	depends_on("r@2.14:", type=("build", "run"))
