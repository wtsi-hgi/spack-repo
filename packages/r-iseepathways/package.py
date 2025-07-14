# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseepathways(RPackage):
	"""iSEE extension for panels related to pathway analysis

	This package contains diverse functionality to extend the usage of the iSEE package, including additional classes for the panels or modes facilitating the analysis of pathway analysis results. This package does not perform pathway analysis. Instead, it provides methods to embed precomputed pathway analysis results in a SummarizedExperiment object, in a manner that is compatible with interactive visualisation in iSEE applications.
	"""
	
	homepage = "https://github.com/iSEE/iSEEpathways"
	bioc = "iSEEpathways" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSEEpathways_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSEEpathways/iSEEpathways_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="ee415ded9e44d0ef1eb82419063d80f71d722d1c069fcb010c17f57bc63b712b")

	depends_on("r-isee", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
