# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedland(RPackage):
	"""RDF Library Bindings in R

	Provides methods to parse, query and serialize information
    stored in the Resource Description Framework (RDF). RDF is described at <https://www.w3.org/TR/rdf-primer/>.
    This package supports RDF by implementing an R interface to the Redland RDF C library,
    described at <https://librdf.org/docs/api/index.html>. In brief, RDF provides a structured graph
    consisting of Statements composed of Subject, Predicate, and Object Nodes.
	"""
	
	homepage = "https://github.com/ropensci/redland-bindings/tree/master/R/redland"
	cran = "redland" 

	version("1.0.17-18", md5="3c94732a635a7338e94e822743f99f3e")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
