# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinylight(RPackage):
	"""Web Interface to 'R' Functions

	Web front end for your 'R' functions producing plots or tables.
    If you have a function or set of related functions, you can make them
    available over the internet through a web browser. This is the same
    motivation as the 'shiny' package, but note that the development of
    'shinylight' is not in any way linked to that of 'shiny' (beyond the use of
    the 'httpuv' package). You might prefer 'shinylight' to 'shiny' if you want
    a lighter weight deployment with easier horizontal scaling, or if you want
    to develop your front end yourself in JavaScript and HTML just using
    a lightweight remote procedure call interface to your R code on the
    server.
	"""
	
	cran = "shinylight" 

	version("1.1.2", md5="7e6f96c24171205efdbabb1facc1fa0c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httpuv@1.5.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-later@1:", type=("build", "run"))
