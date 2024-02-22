# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastnet(RPackage):
	"""Large-Scale Social Network Analysis

	We present an implementation of the algorithms required to simulate
  large-scale social networks and retrieve their most relevant metrics. Details 
  can be found in the accompanying scientific paper on the Journal 
  of Statistical Software, <doi:10.18637/jss.v096.i07>.
	"""
	
	cran = "fastnet" 

	version("1.0.0", md5="44525f206b368b7e0ed1fff8abc2b0fc")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-igraph@1.2:", type=("build", "run"))
	depends_on("r-tidygraph@1.2:", type=("build", "run"))
