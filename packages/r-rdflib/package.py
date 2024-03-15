# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdflib(RPackage):
	"""Tools to Manipulate and Query Semantic Data

	The Resource Description Framework, or 'RDF' is a widely used
             data representation model that forms the cornerstone of the 
             Semantic Web. 'RDF' represents data as a graph rather than 
             the familiar data table or rectangle of relational databases.
             The 'rdflib' package provides a friendly and concise user interface
             for performing common tasks on 'RDF' data, such as reading, writing
             and converting between the various serializations of 'RDF' data,
             including 'rdfxml', 'turtle', 'nquads', 'ntriples', and 'json-ld';
             creating new 'RDF' graphs, and performing graph queries using 'SPARQL'.
             This package wraps the low level 'redland' R package which
             provides direct bindings to the 'redland' C library.  Additionally,
             the package supports the newer and more developer friendly
             'JSON-LD' format through the 'jsonld' package. The package
             interface takes inspiration from the Python 'rdflib' library.
	"""
	
	homepage = "https://github.com/ropensci/rdflib"
	cran = "rdflib" 

	version("0.2.8", md5="99d2f4bd2b9abca67e385cfdeacebf02")

	depends_on("r-redland", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
