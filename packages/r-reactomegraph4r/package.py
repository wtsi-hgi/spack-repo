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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ReactomeGraph4R_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ReactomeGraph4R/ReactomeGraph4R_1.10.0.tar.gz"]

	version("1.10.0", md5="47a818d1c6d25db90a547d315d1189e8")

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
