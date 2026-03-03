# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolrium(RPackage):
	"""General Purpose R Interface to 'Solr'

	Provides a set of functions for querying and parsing data
    from 'Solr' (<https://solr.apache.org/>) 'endpoints' (local and
    remote), including search, 'faceting', 'highlighting', 'stats', and
    'more like this'. In addition, some functionality is included for
    creating, deleting, and updating documents in a 'Solr' 'database'.
	"""
	
	homepage = "https://github.com/ropensci/solrium"
	cran = "solrium" 

	version("1.2.0", md5="8087feb665c5d0885c7490f5c2a58810")

	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-crul@0.4:", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-jsonlite@1:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
