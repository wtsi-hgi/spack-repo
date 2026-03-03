# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsolr(RPackage):
	"""R to Solr Interface

	A comprehensive R API for querying Apache Solr databases.
             A Solr core is represented as a data frame or list that
             supports Solr-side filtering, sorting,
             transformation and aggregation, all through the familiar
             base R API. Queries are processed
             lazily, i.e., a query is only sent to the database when
             the data are required. 
	"""
	
	cran = "rsolr" 

	version("0.0.13", md5="9f4f962ebec11e520efea07068871df8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.1:", type=("build", "run"))
	depends_on("r-restfulr@0.0.2:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-s4vectors@0.14.3:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
