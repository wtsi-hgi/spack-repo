# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVirtuoso(RPackage):
	"""Interface to 'Virtuoso' using 'ODBC'

	Provides users with a simple and convenient
             mechanism to manage and query a 'Virtuoso' database using the 'DBI' (Data-Base Interface)
             compatible 'ODBC' (Open Database Connectivity) interface.
             'Virtuoso' is a high-performance "universal server," which can act
             as both a relational database, supporting standard Structured Query
             Language ('SQL') queries, while also supporting data following the
             Resource Description Framework ('RDF') model for Linked Data.
             'RDF' data can be queried using 'SPARQL' ('SPARQL' Protocol and 'RDF' Query Language)
             queries, a graph-based query that supports semantic reasoning.
             This allows users to leverage the performance of local or remote 'Virtuoso' servers using
             popular 'R' packages such as 'DBI' and 'dplyr', while also providing a 
             high-performance solution for working with large 'RDF' 'triplestores' from 'R.'
             The package also provides helper routines to install, launch, and manage
             a 'Virtuoso' server locally on 'Mac', 'Windows' and 'Linux' platforms using
             the standard interactive installers from the 'R' command-line.  By 
             automatically handling these setup steps, the package can make using 'Virtuoso'
             considerably faster and easier for a most users to deploy in a local
             environment. Managing the bulk import of triples
             from common serializations with a single intuitive command is another key
             feature of this package.  Bulk import performance can be tens to
             hundreds of times faster than the comparable imports using existing 'R' tools,
             including 'rdflib' and 'redland' packages.  
	"""
	
	homepage = "https://github.com/ropensci/virtuoso"
	cran = "virtuoso" 

	version("0.1.8", md5="d6ed9b078c01d03bf3cec5f0ee043f96")

	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-ini", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
	depends_on("virtuoso", type=("build", "link", "run"))
