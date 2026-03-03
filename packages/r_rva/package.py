# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRva(RPackage):
	"""RNAseq Visualization Automation

	Automate downstream visualization & pathway analysis in RNAseq analysis. 'RVA' is a collection of functions that efficiently visualize RNAseq differential expression analysis result from summary statistics tables. It also utilize the Fisher's exact test to evaluate gene set or pathway enrichment in a convenient and efficient manner.
	"""
	
	homepage = "https://github.com/THERMOSTATS/RVA"
	cran = "RVA" 

	version("0.0.5", md5="cc3adabdde3ad52b9de84672fc403622")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gsvadata@1.22:", type=("build", "run"))
	depends_on("r-clusterprofiler@3.15.1:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-edger@3.28.1:", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.10:", type=("build", "run"))
	depends_on("r-complexheatmap@2.2:", type=("build", "run"))
	depends_on("r-gseabase@1.48:", type=("build", "run"))
	depends_on("r-circlize@0.4.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-haven@2.3.1:", type=("build", "run"))
	depends_on("r-msigdbr@7.1.1:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rwikipathways@1.6.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
