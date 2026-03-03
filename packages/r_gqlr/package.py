# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGqlr(RPackage):
	"""'GraphQL' Server in R

	Server implementation of 'GraphQL' <http://graphql.github.io/graphql-spec/>,
    a query language originally created by Facebook for describing data requirements on complex application
    data models.  Visit <http://graphql.org> to learn more about 'GraphQL'.
	"""
	
	homepage = "https://github.com/schloerke/gqlr"
	cran = "gqlr" 

	version("0.0.2", md5="dddc12c1fd189922a3debb6dee7b973f")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-graphql@1.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
