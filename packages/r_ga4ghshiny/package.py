# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGa4ghshiny(RPackage):
	"""Shiny application for interacting with GA4GH-based data servers

	GA4GHshiny package provides an easy way to interact with data servers based on Global Alliance for Genomics and Health (GA4GH) genomics API through a Shiny application. It also integrates with Beacon Network.
	"""
	
	homepage = "https://github.com/labbcb/GA4GHshiny"
	bioc = "GA4GHshiny" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GA4GHshiny_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GA4GHshiny/GA4GHshiny_1.24.0.tar.gz"]

	version("1.24.0", md5="629ca5d338b8435b238169892016d447")

	depends_on("r-ga4ghclient", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
