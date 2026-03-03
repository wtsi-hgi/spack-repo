# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchmulti(RPackage):
	"""Optimal Multilevel Matching using a Network Algorithm

	Performs multilevel matches for data with cluster-
	level treatments and individual-level outcomes using a network 
	optimization algorithm.  Functions for checking balance at the 
	cluster and individual levels are also provided, as are methods 
	for permutation-inference-based outcome analysis.  Details in 
	Pimentel et al. (2018) <doi:10.1214/17-AOAS1118>.  The optmatch 
	package, which is useful for running many of the provided 
	functions, may be downloaded from Github at 
	<https://github.com/markmfredrickson/optmatch> if not available on 
	CRAN.
	"""
	
	cran = "matchMulti" 

	version("1.1.12", md5="317d90bd1aaba8282797bd085efc6d14")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcbsubset@1.1.4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
	depends_on("r-weights", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
