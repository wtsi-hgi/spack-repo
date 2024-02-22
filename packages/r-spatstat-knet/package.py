# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatKnet(RPackage):
	"""Extension to 'spatstat' for Large Datasets on a Linear Network

	Extension to the 'spatstat' family of packages, for analysing
	     large datasets of spatial points on a network. The geometrically-
	     corrected K function is computed using a memory-efficient
	     tree-based algorithm described by Rakshit, Baddeley and Nair (2019).
	"""
	
	cran = "spatstat.Knet" 

	version("3.0-2", md5="35cc03a32093e9ce6c90f51295844676")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat-sparse@3:", type=("build", "run"))
	depends_on("r-spatstat-geom@3:", type=("build", "run"))
	depends_on("r-spatstat-random@3:", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-linnet@3:", type=("build", "run"))
	depends_on("r-spatstat@3:", type=("build", "run"))
	depends_on("r-spatstat-utils@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
