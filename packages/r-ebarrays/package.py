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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBarrays_2.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBarrays/EBarrays_2.66.0.tar.gz"]

	version("2.72.0", tag="RELEASE_3_21")
	version("2.66.0", sha256="f810ddcd8f363086be0df36bebe739785fb228f527822965b9a8a65e69f00dd5")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
