# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocstring(RPackage):
	"""Provides Docstring Capabilities to R Functions

	Provides the ability to display something analogous to
    Python's docstrings within R.  By allowing the user to document
    their functions as comments at the beginning of their function
    without requiring putting the function into a package we allow
    more users to easily provide documentation for their functions.
    The documentation can be viewed just like any other help files
    for functions provided by packages as well.
	"""
	
	homepage = "https://github.com/dasonk/docstring"
	cran = "docstring" 

	version("1.0.0", md5="5f6db2ed9e75f5337a6e6732d7400b14")

	depends_on("r-roxygen2", type=("build", "run"))
