# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RConsensusclusterplus(RPackage):
	"""ConsensusClusterPlus

	algorithm for determining cluster count and membership by stability evidence in unsupervised analysis
	"""
	
	bioc = "ConsensusClusterPlus" 

	version("1.66.0", commit="aa15b11bd487008bf4637c1aee14a618a8c091b6")

	depends_on("r-all", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))

