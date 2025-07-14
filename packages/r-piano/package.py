# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiano(RPackage):
	"""Platform for integrative analysis of omics data

	Piano performs gene set analysis using various statistical methods, from different gene level statistics and a wide range of gene-set collections. Furthermore, the Piano package contains functions for combining the results of multiple runs of gene set analyses.
	"""
	
	homepage = "http://www.sysbio.se/piano"
	bioc = "piano"

	version("2.24.0", commit="6ba9c0980d7484fa4055f19bc039df32533b5b2f")
	version("2.18.0", commit="7c9e20e3481a7e364e876240b2799485530809da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-relations", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
