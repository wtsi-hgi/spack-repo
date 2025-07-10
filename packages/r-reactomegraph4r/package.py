# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomegraph4r(RPackage):
	"""Interface for the Reactome Graph Database

	Pathways, reactions, and biological entities in Reactome knowledge are systematically represented as an ordered network. Instances are represented as nodes and relationships between instances as edges; they are all stored in the Reactome Graph Database. This package serves as an interface to query the interconnected data from a local Neo4j database, with the aim of minimizing the usage of Neo4j Cypher queries.
	"""
	
	homepage = "https://github.com/reactome/ReactomeGraph4R"
	bioc = "ReactomeGraph4R" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReactomeGraph4R_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReactomeGraph4R/ReactomeGraph4R_1.10.0.tar.gz"]

	version("1.10.0", sha256="74ebf29242486e445ae171feda4380268b40a9f8db1cbc66e2c0742aced6543e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-neo4r", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reactomecontentservice4r", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
