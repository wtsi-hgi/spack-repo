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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ConsensusClusterPlus_1.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ConsensusClusterPlus/ConsensusClusterPlus_1.66.0.tar.gz"]

	version("1.66.0", md5="0943cc2a0d1dff314f384e65b8d71897")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-all", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
