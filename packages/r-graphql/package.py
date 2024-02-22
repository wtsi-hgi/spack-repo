# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphql(RPackage):
	"""A GraphQL Query Parser

	Bindings to the 'libgraphqlparser' C++ library. Parses GraphQL syntax
    and exports the AST in JSON format.
	"""
	
	homepage = "https://docs.ropensci.org/graphql/"
	cran = "graphql" 

	version("1.5.1", md5="351082220b92fa28101d923075ed57d1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
