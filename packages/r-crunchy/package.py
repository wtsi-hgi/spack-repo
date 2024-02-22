# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrunchy(RPackage):
	"""Shiny Apps on Crunch

	To facilitate building custom dashboards on the Crunch data
    platform <https://crunch.io/>, the 'crunchy' package provides tools for
    working with 'shiny'. These tools include utilities to manage authentication
    and authorization automatically and custom stylesheets to help match the
    look and feel of the Crunch web application. The package also includes
    several gadgets for use in 'RStudio'.
	"""
	
	homepage = "https://crunch.io/r/crunchy/"
	cran = "crunchy" 

	version("0.3.3", md5="ea3b7623efda07da7aa612042d1e4a3a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-crunch", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-httpcache", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-rstudioapi@0.4:", type=("build", "run"))
