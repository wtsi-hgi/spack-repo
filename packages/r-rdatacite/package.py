# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdatacite(RPackage):
	"""Client for the 'DataCite' API

	Client for the web service methods provided by 'DataCite'
    (<https://www.datacite.org/>), including functions to interface with
    their 'RESTful' search API. The API is backed by 'Elasticsearch',
    allowing expressive queries, including faceting.
	"""
	
	homepage = "https://docs.ropensci.org/rdatacite/"
	cran = "rdatacite" 

	version("0.5.4", md5="09aaf2e2db0a25900dd8c7428d68a692")

	depends_on("r-crul@0.7.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
