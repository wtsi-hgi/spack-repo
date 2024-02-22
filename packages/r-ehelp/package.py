# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhelp(RPackage):
	"""Enhanced Help to Enable "Docstring"-Comments in Users Functions

	By overloading the R help() function, this package allows users to use "docstring" style comments within their own defined functions. The package also provides additional functions to mimic the R basic example() function and the prototyping of packages.
	"""
	
	homepage = "https://github.com/mponce0/eHelp"
	cran = "ehelp" 

	version("1.2.1", md5="273d2eb201135240117d5a6c4e50daa8")

