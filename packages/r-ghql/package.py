# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhql(RPackage):
	"""General Purpose 'GraphQL' Client

	A 'GraphQL' client, with an R6 interface for initializing
    a connection to a 'GraphQL' instance, and methods for constructing
    queries, including fragments and parameterized queries. Queries
    are checked with the 'libgraphqlparser' C++ parser via the
    'gaphql' package.
	"""
	
	homepage = "https://github.com/ropensci/ghql"
	cran = "ghql" 

	version("0.1.0", md5="39a6661c34853cad7ef1a14d91709267")

	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-graphql", type=("build", "run"))
