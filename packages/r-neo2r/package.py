# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeo2r(RPackage):
	"""Neo4j to R

	The aim of neo2R is to provide simple and low level connectors
   for querying neo4j graph databases (<https://neo4j.com/>).
   The objects returned by the query functions are either lists or data.frames
   with very few post-processing.
   It allows fast processing of queries returning many records.
   And it let the user handle post-processing according to the data model
   and his needs.
	"""
	
	homepage = "https://github.com/patzaw/neo2r"
	cran = "neo2R" 

	version("2.4.2", md5="f91f18f265df185005e89fb24e0d9587")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("neo4j@3:6", type=("build", "link", "run"))
