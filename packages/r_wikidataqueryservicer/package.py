# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikidataqueryservicer(RPackage):
	"""API Client Library for 'Wikidata Query Service'

	An API client for the 'Wikidata Query Service'
    <https://query.wikidata.org/>.
	"""
	
	homepage = "https://github.com/bearloga/WikidataQueryServiceR"
	cran = "WikidataQueryServiceR" 

	version("1.0.0", md5="525223b28b64f607b312d0faf15990b4")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.2:", type=("build", "run"))
	depends_on("r-wikipedir@1.5:", type=("build", "run"))
	depends_on("r-ratelimitr@0.4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rex@1.2:", type=("build", "run"))
