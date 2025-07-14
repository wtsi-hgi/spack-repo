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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/piano_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/piano/piano_2.18.0.tar.gz"]

	version("2.24.0", tag="RELEASE_3_21")
	version("2.18.0", sha256="be50b0dd78b8421bf2fd018a381f699a59d628303d83f0fc1471af3b5e2c8567")

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
