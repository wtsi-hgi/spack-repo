# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegionereloaded(RPackage):
	"""RegioneReloaded: Multiple Association for Genomic Region Sets

	RegioneReloaded is a package that allows simultaneous analysis of associations between genomic region sets, enabling clustering of data and the creation of ready-to-publish graphs. It takes over and expands on all the features of its predecessor regioneR. It also incorporates a strategy to improve p-value calculations and normalize z-scores coming from multiple analysis to allow for their direct comparison. RegioneReloaded builds upon regioneR by adding new plotting functions for obtaining publication-ready graphs.
	"""
	
	homepage = "https://github.com/RMalinverni/regioneReload"
	bioc = "regioneReloaded" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/regioneReloaded_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/regioneReloaded/regioneReloaded_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="5403ee99be6a27a97e3def6161f92fda138f14bf30662b56581ad07fd4024c15")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
