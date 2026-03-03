# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollidr(RPackage):
	"""Check for Namespace Collisions Across Packages and Functions on
CRAN

	Check for namespace collisions between a string input (your function or package name) 
    and half a million packages and functions on CRAN.
	"""
	
	homepage = "https://github.com/collidrpackage/collidr"
	cran = "collidr" 

	version("0.1.3", md5="487edb47fd5e36d9eadfef388bb27721")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
