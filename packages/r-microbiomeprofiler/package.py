# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiomeprofiler(RPackage):
	"""An R/shiny package for microbiome functional enrichment analysis

	This is an R/shiny package to perform functional enrichment analysis for microbiome data. This package was based on clusterProfiler. Moreover, MicrobiomeProfiler support KEGG enrichment analysis, COG enrichment analysis, Microbe-Disease association enrichment analysis, Metabo-Pathway analysis.
	"""
	
	homepage = "https://github.com/YuLab-SMU/MicrobiomeProfiler/"
	bioc = "MicrobiomeProfiler"

	version("1.14.0", commit="e2042a0d7410dbbf9adc0a8b36c9ba770504ca50")
	version("1.8.0", commit="4aff8e768d990b8b2784b112de8fc0060775b607")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-clusterprofiler@4.5.2:", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-gson", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinycustomloader", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
