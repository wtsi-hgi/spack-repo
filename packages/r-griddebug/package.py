# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGriddebug(RPackage):
	"""Debugging 'grid' Graphics

	Functions for drawing scene trees representing 
              scenes that have been drawn using grid graphics.
	"""
	
	cran = "gridDebug" 

	version("0.5-1", md5="46abf53a0e9fa2f86083d9a777d5a1ed")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-gridgraphviz", type=("build", "run"))
	depends_on("r-gridsvg@1.1:", type=("build", "run"))
	depends_on("graphviz", type=("build", "link", "run"))
