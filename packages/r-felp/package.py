# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFelp(RPackage):
	"""Functional Help for Functions, Objects, and Packages

	
    Enhance R help system by fuzzy search and preview interface, pseudo-postfix operators, and more.
    The `?.` pseudo-postfix operator and the `?` prefix operator displays documents and contents (source or structure) of objects simultaneously to help understanding the objects.
    The `?p` pseudo-postfix operator displays package documents, and is shorter than help(package = foo).
	"""
	
	homepage = "https://github.com/atusy/felp"
	cran = "felp" 

	version("0.4.0", md5="f14584822fd470e9eb24a0f30e02cf05")

	depends_on("r-prettycode", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-reactable", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
