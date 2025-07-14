# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicsviewer(RPackage):
	"""Interactive and explorative visualization of SummarizedExperssionSet or ExpressionSet using omicsViewer

	omicsViewer visualizes ExpressionSet (or SummarizedExperiment) in an interactive way. The omicsViewer has a separate back- and front-end. In the back-end, users need to prepare an ExpressionSet that contains all the necessary information for the downstream data interpretation. Some extra requirements on the headers of phenotype data or feature data are imposed so that the provided information can be clearly recognized by the front-end, at the same time, keep a minimum modification on the existing ExpressionSet object. The pure dependency on R/Bioconductor guarantees maximum flexibility in the statistical analysis in the back-end. Once the ExpressionSet is prepared, it can be visualized using the front-end, implemented by shiny and plotly. Both features and samples could be selected from (data) tables or graphs (scatter plot/heatmap). Different types of analyses, such as enrichment analysis (using Bioconductor package fgsea or fisher's exact test) and STRING network analysis, will be performed on the fly and the results are visualized simultaneously. When a subset of samples and a phenotype variable is selected, a significance test on means (t-test or ranked based test; when phenotype variable is quantitative) or test of independence (chi-square or fisher’s exact test; when phenotype data is categorical) will be performed to test the association between the phenotype of interest with the selected samples. Additionally, other analyses can be easily added as extra shiny modules. Therefore, omicsViewer will greatly facilitate data exploration, many different hypotheses can be explored in a short time without the need for knowledge of R. In addition, the resulting data could be easily shared using a shiny server. Otherwise, a standalone version of omicsViewer together with designated omics data could be easily created by integrating it with portable R, which can be shared with collaborators or submitted as supplementary data together with a manuscript.
	"""
	
	homepage = "https://github.com/mengchen18/omicsViewer"
	bioc = "omicsViewer" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/omicsViewer_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/omicsViewer/omicsViewer_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="e5a3f73a0ab5cac65eb8b341aae0ba77910aefd9c7e64042634e9b37748a4dd5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-beeswarm", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-flatxml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-ggseqlogo", type=("build", "link", "run"))
