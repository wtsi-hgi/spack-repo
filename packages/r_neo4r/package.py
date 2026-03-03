# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeo4r(RPackage):
	"""A 'Neo4J' Driver

	A Modern and Flexible 'Neo4J' Driver, allowing you to query 
    data on a 'Neo4J' server and handle the results in R. It's modern in 
    the sense it provides a driver 
    that can be easily integrated in a data analysis workflow, especially by 
    providing an API working smoothly with other data analysis and graph 
    packages. It's flexible in the  way it returns the results, by 
    trying to stay as close as 
    possible to the way 'Neo4J' returns data. That way, you have the control 
    over the way you will compute the results. At the same time, the result 
    is not too complex, so that the "heavy lifting" of data wrangling is not 
    left to the user. 
	"""
	
	homepage = "https://github.com/neo4j-rstats/neo4r"
	cran = "neo4r" 

	version("0.1.1", md5="75ab01a161c8a90279e7bee09136431b")

	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
