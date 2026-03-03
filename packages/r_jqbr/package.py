# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJqbr(RPackage):
	"""'jQuery QueryBuilder' Input for 'Shiny'

	A highly configurable 'jQuery' plugin offering a simple
    interface to create complex queries/filters in 'Shiny'. The outputted
    rules can easily be parsed into a set of 'R' and/or 'SQL' queries and
    used to filter data. Custom parsing of the rules is also supported.
    For more information about 'jQuery QueryBuilder' see
    <https://querybuilder.js.org/>.
	"""
	
	homepage = "https://github.com/hfshr/jqbr"
	cran = "jqbr" 

	version("1.0.3", md5="4b5fafc955550b49eafafbff97dc7be8")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
