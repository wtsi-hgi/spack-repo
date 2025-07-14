# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpotclean(RPackage):
	"""SpotClean adjusts for spot swapping in spatial transcriptomics data

	SpotClean is a computational method to adjust for spot swapping in spatial transcriptomics data. Recent spatial transcriptomics experiments utilize slides containing thousands of spots with spot-specific barcodes that bind mRNA. Ideally, unique molecular identifiers at a spot measure spot-specific expression, but this is often not the case due to bleed from nearby spots, an artifact we refer to as spot swapping. SpotClean is able to estimate the contamination rate in observed data and decontaminate the spot swapping effect, thus increase the sensitivity and precision of downstream analyses.
	"""
	
	homepage = "https://github.com/zijianni/SpotClean"
	bioc = "SpotClean" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpotClean_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpotClean/SpotClean_1.4.1.tar.gz"]

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.1", sha256="64b09ee1226b18db386581e2a73b7557780711583f2d83f03b4ea7f51734ca1a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
