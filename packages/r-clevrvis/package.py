# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClevrvis(RPackage):
	"""Visualization Techniques for Clonal Evolution

	clevRvis provides a set of visualization techniques for clonal evolution. These include shark plots, dolphin plots and plaice plots. Algorithms for time point interpolation as well as therapy effect estimation are provided. Phylogeny-aware color coding is implemented. A shiny-app for generating plots interactively is additionally provided.
	"""
	
	homepage = "https://github.com/sandmanns/clevRvis"
	bioc = "clevRvis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clevRvis_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clevRvis/clevRvis_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="b40c4fe95a6b56bd73ccdaa87e5075600158db4399a3374665b1e220183cf55c")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
