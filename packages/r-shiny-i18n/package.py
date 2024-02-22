# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyI18n(RPackage):
	"""Shiny Applications Internationalization

	It provides easy internationalization of Shiny
    applications. It can be used as standalone translation package
    to translate reports, interactive visualizations or
    graphical elements as well.
	"""
	
	homepage = "https://appsilon.github.io/shiny.i18n/"
	cran = "shiny.i18n" 

	version("0.3.0", md5="f17d036969c1839c3fad60d4f9aad1dd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
