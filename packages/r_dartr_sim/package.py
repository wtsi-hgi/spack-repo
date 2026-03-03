# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDartrSim(RPackage):
	"""Computer Simulations of 'SNP' Data

	Allows to simulate SNP data using genlight objects. For example, it is straight forward to simulate a simple drift scenario with exchange of individuals between two populations or create a new genlight object based on allele frequencies of an existing genlight object.
	"""
	
	homepage = "https://green-striped-gecko.github.io/dartR/"
	cran = "dartR.sim" 

	version("0.70", md5="265e9c8cb527b121b24ca20da2ae46b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adegenet@2:", type=("build", "run"))
	depends_on("r-dartr-base", type=("build", "run"))
	depends_on("r-dartr-data", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-hierfstat", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
