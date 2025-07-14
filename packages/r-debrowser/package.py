# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebrowser(RPackage):
	"""Interactive Differential Expresion Analysis Browser

	Bioinformatics platform containing interactive plots and tables for differential gene and region expression studies. Allows visualizing expression data much more deeply in an interactive and faster way. By changing the parameters, users can easily discover different parts of the data that like never have been done before. Manually creating and looking these plots takes time. With DEBrowser users can prepare plots without writing any code. Differential expression, PCA and clustering analysis are made on site and the results are shown in various plots such as scatter, bar, box, volcano, ma plots and Heatmaps.
	"""
	
	homepage = "https://github.com/UMMS-Biocore/debrowser"
	bioc = "debrowser" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/debrowser_1.30.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/debrowser/debrowser_1.30.2.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.2", sha256="5dc2e79bf02010d18b321b5f735fc306cb1744dc8df7deefc73eb0deb5eca53a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-harman", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-apeglm", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
