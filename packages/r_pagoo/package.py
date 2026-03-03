# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagoo(RPackage):
	"""Analyze Bacterial Pangenomes in R with 'Pagoo'

	Provides an encapsulated, object-oriented class system for
  analyzing bacterial pangenomes. For a definition of this concept, see
  Tettelin, et al. (2005) <doi:10.1073/pnas.0506758102>. It uses the R6
  package as backend. It was designed in order to facilitate and speed-up
  the comparative analysis of multiple bacterial genomes, standardizing and
  optimizing routine tasks performed everyday. There are a handful of things
  done everyday when working with bacterial pangenomes: subset, summarize,
  extract, visualize and store data. So, 'pagoo' is intended to facilitate these
  tasks as much as possible. For a description of the implemented data structure
  and methods, see Ferres & Iraola (2020), <doi:10.1101/2020.07.29.226951>.
	"""
	
	homepage = "https://iferres.github.io/pagoo/"
	cran = "pagoo" 

	version("0.3.17", md5="e6735f974e54be36a0b083cd3846678f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
