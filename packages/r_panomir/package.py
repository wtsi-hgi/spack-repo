# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanomir(RPackage):
	"""Detection of miRNAs that regulate interacting groups of pathways

	PanomiR is a package to detect miRNAs that target groups of pathways from gene expression data. This package provides functionality for generating pathway activity profiles, determining differentially activated pathways between user-specified conditions, determining clusters of pathways via the PCxN package, and generating miRNAs targeting clusters of pathways. These function can be used separately or sequentially to analyze RNA-Seq data.
	"""
	
	homepage = "https://github.com/pouryany/PanomiR"
	bioc = "PanomiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PanomiR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PanomiR/PanomiR_1.6.0.tar.gz"]

	version("1.6.0", md5="a8f96cdc267551107e69e8cb260a05c0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
