# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgraphinshiny(RPackage):
	"""Use 'shiny' to Demo 'igraph'

	Using 'shiny' to demo 'igraph' package makes learning graph theory easy and fun.
	"""
	
	cran = "igraphinshiny" 

	version("0.1", md5="d8421910df1fc8055d03a3aab968e59f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
