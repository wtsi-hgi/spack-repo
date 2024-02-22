# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeal(RPackage):
	"""Interactive Differential Expression AnaLysis

	This package provides functions for an Interactive Differential Expression AnaLysis of RNA-sequencing datasets, to extract quickly and effectively information downstream the step of differential expression. A Shiny application encapsulates the whole package.
	"""
	
	homepage = "https://github.com/federicomarini/ideal"
	bioc = "ideal" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ideal_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ideal/ideal_1.26.0.tar.gz"]

	version("1.26.0", md5="d4714305a9be71a4b4c71da0fb624148")

	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-pcaexplorer", type=("build", "run"))
	depends_on("r-ihw", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-goseq", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-shiny@0.12:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
