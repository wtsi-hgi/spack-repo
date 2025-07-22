# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcaexplorer(RPackage):
	"""Interactive Visualization of RNA-seq Data Using a Principal Components Approach

	This package provides functionality for interactive visualization of RNA-seq datasets based on Principal Components Analysis. The methods provided allow for quick information extraction and effective data exploration. A Shiny application encapsulates the whole analysis.
	"""
	
	homepage = "https://github.com/federicomarini/pcaExplorer"
	bioc = "pcaExplorer"

	version("3.2.0", commit="c394b92262f05d27bf83d3ff28eacec9c0b9efd1")
	version("2.28.0", commit="bc5fa86250a1d7842586cd9e22d4b591bbcb2359")

	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-shiny@0.12:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-threejs", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
