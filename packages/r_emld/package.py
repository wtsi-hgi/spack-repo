# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmld(RPackage):
	"""Ecological Metadata as Linked Data

	This is a utility for transforming Ecological Metadata Language
        ('EML') files into 'JSON-LD' and back into 'EML.'  Doing so creates a
        list-based representation of 'EML' in R, so that 'EML' data can easily
        be manipulated using standard 'R' tools. This makes this package an
        effective backend for other 'R'-based tools  working with 'EML.' By
        abstracting away the complexity of 'XML' Schema, developers can
        build around native 'R' list objects and not have to worry about satisfying
        many of the additional constraints of set by the schema (such as element
        ordering, which is handled automatically). Additionally, the 'JSON-LD' 
        representation enables the use of developer-friendly 'JSON' parsing and
        serialization that may facilitate the use of 'EML' in contexts outside of 'R,'
        as well as the informatics-friendly serializations such as 'RDF' and
        'SPARQL' queries.
	"""
	
	homepage = "https://docs.ropensci.org/emld/"
	cran = "emld" 

	version("0.5.1", md5="e332b3ded47fff5574ee5c2bd0c01b0e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonld", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
