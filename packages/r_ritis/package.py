# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitis(RPackage):
	"""Integrated Taxonomic Information System Client

	An interface to the Integrated Taxonomic Information System ('ITIS')
    (<https://www.itis.gov>). Includes functions to work with the 'ITIS' REST
    API methods (<https://www.itis.gov/ws_description.html>), as well as the
    'Solr' web service (<https://www.itis.gov/solr_documentation.html>).
	"""
	
	homepage = "https://github.com/ropensci/ritis"
	cran = "ritis" 

	version("1.0.0", md5="aa35eb23a66b7a7ea0597b239740b65a")

	depends_on("r-solrium@1.1.4:", type=("build", "run"))
	depends_on("r-crul@0.9:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
