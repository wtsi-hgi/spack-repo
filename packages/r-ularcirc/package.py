# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUlarcirc(RPackage):
	"""Shiny app for canonical and back splicing analysis (i.e. circular and mRNA analysis)

	Ularcirc reads in STAR aligned splice junction files and provides visualisation and analysis tools for splicing analysis. Users can assess backsplice junctions and forward canonical junctions.
	"""
	
	bioc = "Ularcirc"

	version("1.26.0", commit="e5a5938dc2c7da51e4068de6fe29447d08a4f19b")
	version("1.20.0", commit="65fe0811ce6a580c873a6c1f53810e32daa855e0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomeinfodbdata", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-mirbase-db", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-organism-dplyr", type=("build", "run"))
	depends_on("r-plotgardener", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
