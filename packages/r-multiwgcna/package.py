# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiwgcna(RPackage):
	"""multiWGCNA

	An R package for deeping mining gene co-expression networks in multi-trait expression data. Provides functions for analyzing, comparing, and visualizing WGCNA networks across conditions. multiWGCNA was designed to handle the common case where there are multiple biologically meaningful sample traits, such as disease vs wildtype across development or anatomical region.
	"""
	
	bioc = "multiWGCNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multiWGCNA_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multiWGCNA/multiWGCNA_1.0.0.tar.gz"]

	version("1.0.0", sha256="c3eebe34ffd6364531b5b768c7b5e87d10f657cd688495a05885d0307855e8ca")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-flashclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dcanr", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
