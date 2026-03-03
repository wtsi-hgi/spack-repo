# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglenlp(RPackage):
	"""An Interface to Google's Cloud Natural Language API

	Interact with Google's Cloud Natural Language API
    <https://cloud.google.com/natural-language/> (v1) via R. The API has
    four main features, all of which are available through this
    R package: syntax analysis and part-of-speech tagging, entity
    analysis, sentiment analysis, and language identification.
	"""
	
	homepage = "https://github.com/BrianWeinstein/googlenlp"
	cran = "googlenlp" 

	version("0.2.0", md5="494efcc5b2fdbcf8c96eb8015fc0a437")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
