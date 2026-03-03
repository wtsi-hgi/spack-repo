# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatgraphs(RPackage):
	"""Graph Edge Computations for Spatial Point Patterns

	Graphs (or networks) and graph component
        calculations for spatial locations in 1D, 2D, 3D etc.
	"""
	
	cran = "spatgraphs" 

	version("3.4", md5="bd495becf14d6f3e4dd4a496559f85d5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
