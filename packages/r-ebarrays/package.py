# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbarrays(RPackage):
	"""Unified Approach for Simultaneous Gene Clustering and Differential Expression Identification

	EBarrays provides tools for the analysis of replicated/unreplicated microarray data.
	"""
	
	bioc = "EBarrays" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EBarrays_2.66.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EBarrays/EBarrays_2.66.0.tar.gz"]

	version("2.66.0", md5="d273e2e9411207653d4e079e14484026")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
