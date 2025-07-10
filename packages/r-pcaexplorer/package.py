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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pcaExplorer_2.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pcaExplorer/pcaExplorer_2.28.0.tar.gz"]

	version("2.28.0", sha256="07b0796b684a0801fc38f3a922464acb8e935c739f75f6dc25d4022fb14c0c46")

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
