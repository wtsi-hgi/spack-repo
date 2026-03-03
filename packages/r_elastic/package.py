# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElastic(RPackage):
	"""General Purpose Interface to 'Elasticsearch'

	Connect to 'Elasticsearch', a 'NoSQL' database built on the 'Java'
    Virtual Machine. Interacts with the 'Elasticsearch' 'HTTP' API
    (<https://www.elastic.co/elasticsearch/>), including functions for
    setting connection details to 'Elasticsearch' instances, loading bulk data,
    searching for documents with both 'HTTP' query variables and 'JSON' based body
    requests. In addition, 'elastic' provides functions for interacting with API's
    for 'indices', documents, nodes, clusters, an interface to the cat API, and
    more.
	"""
	
	homepage = "https://docs.ropensci.org/elastic/"
	cran = "elastic" 

	version("1.2.0", md5="9255693af846f296cfdbe567e0a6157d")

	depends_on("r-curl@2.2:", type=("build", "run"))
	depends_on("r-crul@0.9:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
