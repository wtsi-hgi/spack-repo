# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNodbi(RPackage):
	"""'NoSQL' Database Connector

	Simplified document database access and manipulation,
     providing a common API across supported 'NoSQL' databases 
     'Elasticsearch', 'CouchDB', 'MongoDB' as well as 
     'SQLite/JSON1', 'PostgreSQL', and 'DuckDB'.
	"""
	
	homepage = "https://docs.ropensci.org/nodbi/"
	cran = "nodbi" 

	version("0.10.4", md5="2fe15dc9a8dc031cecd83ce1a9945333")
	version("0.10.1", md5="724cc5bfb55b0c06c1f1b88cc8c7845f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-jqr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
