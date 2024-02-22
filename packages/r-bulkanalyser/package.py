# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBulkanalyser(RPackage):
	"""Interactive Shiny App for Bulk Sequencing Data

	Given an expression matrix from a bulk sequencing experiment,
        pre-processes it and creates a shiny app for interactive data 
        analysis and visualisation. The app contains quality checks,
        differential expression analysis, volcano and cross plots,
        enrichment analysis and gene regulatory network inference,
        and can be customised to contain more panels by the user.
	"""
	
	homepage = "https://github.com/Core-Bioinformatics/bulkAnalyseR"
	cran = "bulkAnalyseR" 

	version("1.1.0", md5="4237529b6f084018e02b8bdf247d92cb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-gprofiler2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyjqui", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-noisyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggrastr", type=("build", "run"))
	depends_on("r-genie3", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinylp", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggvenndiagram", type=("build", "run"))
