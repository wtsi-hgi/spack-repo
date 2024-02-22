# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSusographql(RPackage):
	"""Comprehensive Interface to the Survey Solutions 'GraphQL' API

	Provides a complete suite of tools for interacting
    with the Survey Solutions 'GraphQL' API
    <https://demo.mysurvey.solutions/graphql/>. This package encompasses
    all currently available queries and mutations, including the latest
    features for map uploads. It is built on the modern 'httr2' package,
    offering a streamlined and efficient interface without relying on
    external 'GraphQL' client packages. In addition to core API
    functionalities, the package includes a range of helper functions
    designed to facilitate the use of available query filters.
	"""
	
	homepage = "https://michael-cw.github.io/susographql/"
	cran = "susographql" 

	version("0.1.6", md5="f03490be88e7ae16000eae697ad56345")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl@5.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
