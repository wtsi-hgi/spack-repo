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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ConsensusClusterPlus_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ConsensusClusterPlus/ConsensusClusterPlus_1.66.0.tar.gz"]

	version("1.66.0", sha256="bae72341fbc941456a94d67b890139fa98a8de645b38c4d0b771bc4a56faac87")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-all", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
