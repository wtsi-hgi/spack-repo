# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloprofiledata(RPackage):
	"""Data package for phylogenetic profile analysis using PhyloProfile tool

	Two experimental datasets to illustrate running and analysing phylogenetic profiles with PhyloProfile package.
	"""
	
	homepage = "https://github.com/BIONF/PhyloProfileData"
	bioc = "PhyloProfileData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PhyloProfileData_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PhyloProfileData/PhyloProfileData_1.16.0.tar.gz"]

	version("1.16.0", md5="68dda32e9151c0aba4eb5b29c0313f83")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))

	# experiment