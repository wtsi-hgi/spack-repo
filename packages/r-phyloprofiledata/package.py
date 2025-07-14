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

    version("1.22.3", tag="RELEASE_3_21")
	version("1.16.0", sha256="d9959903e225c08a4a5ac8b67bc721fa34f099359f9f14a331fc585477fea1e4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))

