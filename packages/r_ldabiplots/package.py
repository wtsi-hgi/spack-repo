# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdabiplots(RPackage):
	"""Biplot Graphical Interface for LDA Models

	Contains the development of a tool that provides a web-based graphical
             user interface (GUI) to perform Biplots representations from a scraping of
             news from digital newspapers under the Bayesian approach of Latent Dirichlet 
             Assignment (LDA) and machine learning algorithms. Contains LDA methods 
             described by Blei , David M., Andrew Y. Ng and Michael I. Jordan (2003) 
             <https://jmlr.org/papers/volume3/blei03a/blei03a.pdf>,
             and Biplot methods described by Gabriel K.R(1971) <doi:10.1093/biomet/58.3.453>
             and Galindo-Villardon P(1986) <https://diarium.usal.es/pgalindo/files/2012/07/Questiio.pdf>.
	"""
	
	cran = "LDABiplots" 

	version("0.1.2", md5="5e80a4b8b178a6841a63b732f1e63f60")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-ldatuning", type=("build", "run"))
	depends_on("r-topicmodels", type=("build", "run"))
	depends_on("r-textminer", type=("build", "run"))
	depends_on("r-chinese-misc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-textplot", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
