# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyrss(RPackage):
	"""Tidy RSS for R

	
    With the objective of including data from RSS feeds into your analysis, 
    'tidyRSS' parses RSS, Atom and JSON feeds and returns a tidy data frame.
	"""
	
	homepage = "https://github.com/RobertMyles/tidyrss"
	cran = "tidyRSS" 

	version("2.0.7", md5="9e7d819ecb11cb38597440c313a73504")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml2@1.3.1:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-anytime@0.3.7:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
