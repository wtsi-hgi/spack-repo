# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMd4r(RPackage):
	"""Markdown Parser Implemented using the 'MD4C' Library

	Provides an R wrapper for the 'MD4C' (Markdown for 'C') library. 
    Functions exist for parsing markdown ('CommonMark' compliant) along with support for other common
    markdown extensions (e.g. GitHub flavored markdown, 'LaTeX' equation support, etc.). The 
    package also provides a number of higher level functions for exploring and manipulating markdown
    abstract syntax trees as well as translating and displaying the documents.
	"""
	
	cran = "md4r" 

	version("0.5.2.0", md5="3d8e442a876fd42861cae1851d5a46b3")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
