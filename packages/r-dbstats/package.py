# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbstats(RPackage):
	"""Distance-Based Statistics

	Prediction methods where explanatory information is coded as a matrix of distances between individuals. Distances can either be directly input as a distances matrix, a squared distances matrix, an inner-products matrix or computed from observed predictors. 
	"""
	
	cran = "dbstats" 

	version("2.0.2", md5="b8b430eaee71874c61803fc01379a964")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
