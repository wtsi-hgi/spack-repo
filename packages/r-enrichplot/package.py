# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichplot(RPackage):
	"""Visualization of Functional Enrichment Result.

	The 'enrichplot' package implements several visualization methods for
	interpreting functional enrichment results obtained from ORA or GSEA
	analysis. All the visualization methods are developed based on 'ggplot2'
	graphics."""

	bioc = "enrichplot"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/enrichplot_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/enrichplot/enrichplot_1.22.0.tar.gz"]

	version("1.22.0", md5="4accfec43292c11ec0165092f3266ac2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aplot@0.2.1:", type=("build", "run"))
	depends_on("r-dose@3.16:", type=("build", "run"))
	depends_on("r-ggfun@0.1.3:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scatterpie", type=("build", "run"))
	depends_on("r-shadowtext", type=("build", "run"))
	depends_on("r-gosemsim", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggtree", type=("build", "run"))
	depends_on("r-yulab-utils@0.0.8:", type=("build", "run"))
