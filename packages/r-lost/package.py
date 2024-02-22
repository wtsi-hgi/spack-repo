# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLost(RPackage):
	"""Missing Morphometric Data Simulation and Estimation

	Functions for simulating missing morphometric
	data randomly, with taxonomic bias and with anatomical bias. LOST also 
	includes functions for estimating linear and geometric morphometric data. 
	"""
	
	cran = "LOST" 

	version("2.0.2", md5="abd9aefb6d3cfa32552db385ba82bed3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-misctools", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-geomorph", type=("build", "run"))
