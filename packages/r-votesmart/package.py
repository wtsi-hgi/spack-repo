# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVotesmart(RPackage):
	"""Wrapper for the Project 'VoteSmart' API

	An R interface to the Project 'VoteSmart'<https://justfacts.votesmart.org/> API.
	"""
	
	homepage = "https://github.com/decktools/votesmart/"
	cran = "votesmart" 

	version("0.1.2", md5="1d9bc4a1dac7f1b259917726b9994955")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-snakecase@0.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
