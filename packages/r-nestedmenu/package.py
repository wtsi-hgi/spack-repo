# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestedmenu(RPackage):
	"""A Nested Menu Widget for 'Shiny' Applications

	Provides a nested menu widget for usage in 'Shiny'
    applications. This is useful for hierarchical choices (e.g. continent,
    country, city).
	"""
	
	homepage = "https://github.com/stla/NestedMenu"
	cran = "NestedMenu" 

	version("0.2.0", md5="49df469f7ea3c5b6ca22c550458c75a2")

	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jquerylib", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
