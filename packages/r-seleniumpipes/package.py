# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeleniumpipes(RPackage):
	"""R Client Implementing the W3C WebDriver Specification

	The W3C WebDriver specification defines a way for out-of-process
    programs to remotely instruct the behaviour of web browsers. It is detailed
    at <https://w3c.github.io/webdriver/webdriver-spec.html>. This package provides
    an R client implementing the W3C specification.
	"""
	
	homepage = "https://github.com/johndharrison/seleniumPipes"
	cran = "seleniumPipes" 

	version("0.3.7", md5="b56a48df619794995d350e868a072caa")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
