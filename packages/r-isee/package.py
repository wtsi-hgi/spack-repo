# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsee(RPackage):
	"""Interactive SummarizedExperiment Explorer

	Create an interactive Shiny-based graphical user interface for exploring data stored in SummarizedExperiment objects, including row- and column-level metadata. The interface supports transmission of selections between plots and tables, code tracking, interactive tours, interactive or programmatic initialization, preservation of app state, and extensibility to new panel types via S4 classes. Special attention is given to single-cell data in a SingleCellExperiment object with visualization of dimensionality reduction results.
	"""
	
	homepage = "https://github.com/iSEE/iSEE"
	bioc = "iSEE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSEE_2.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSEE/iSEE_2.14.0.tar.gz"]

	version("2.14.0", sha256="44b2ecfea6f47e414b372c04e68be5384e873336c7caffb6b07a206905d71e4e")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-vipor", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
