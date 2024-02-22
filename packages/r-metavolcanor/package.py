# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetavolcanor(RPackage):
	"""Gene Expression Meta-analysis Visualization Tool

	MetaVolcanoR combines differential gene expression results. It implements three strategies to summarize differential gene expression from different studies. i) Random Effects Model (REM) approach, ii) a p-value combining-approach, and iii) a vote-counting approach. In all cases, MetaVolcano exploits the Volcano plot reasoning to visualize the gene expression meta-analysis results.
	"""
	
	bioc = "MetaVolcanoR" 

	version("1.16.0", commit="9f793a444c6d9b80d7c4167c70f0a8e00cb92372")

	depends_on("r@4.1.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-topconfects", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
