# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJs(RPackage):
	"""Tools for Working with JavaScript in R

	A set of utilities for working with JavaScript syntax in R.
    Includes tools to parse, tokenize, compile, validate, reformat, optimize 
    and analyze JavaScript code.
	"""
	
	homepage = "https://github.com/jeroen/js"
	cran = "js" 

	version("1.2", md5="f2d96d19f36d9d1b9cbc12e2f43eb753")

	depends_on("r-v8@0.5:", type=("build", "run"))
