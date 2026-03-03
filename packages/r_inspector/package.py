# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspector(RPackage):
	"""Validation of Arguments and Objects in User-Defined Functions

	Utility functions that implement and automate common sets of validation tasks. 
    These functions are particularly useful to validate inputs, intermediate objects and output 
    values in user-defined functions, resulting in tidier and less verbose functions.
	"""
	
	homepage = "https://ptfonseca.github.io/inspector/"
	cran = "inspector" 

	version("1.0.3", md5="92cd2862b81f9263fb6465163fd17625")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
