# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikkitidy(RPackage):
	"""Tidy Analysis of Wikipedia

	Access 'Wikipedia' through the several 'MediaWiki' APIs
    (<https://www.mediawiki.org/wiki/API>), as well as through the
    'XTools' API (<https://www.mediawiki.org/wiki/XTools/API>). Ensure
    your API calls are correct, and receive results in tidy tibbles.
	"""
	
	homepage = "https://wikihistories.github.io/wikkitidy/"
	cran = "wikkitidy" 

	version("0.1.12", md5="85693739bc91c46138e4fa5ad6288647")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
