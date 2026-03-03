# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemverutils(RPackage):
	"""Semantic Version Utilities

	Semantic Versions allow for standardized management versions. 
    This package implements semantic versioning handling in R. using R6 to 
    create a mutable object that can handle deciphering and checking versions. 
	"""
	
	homepage = "https://github.com/ajwtech/semverutils"
	cran = "semverutils" 

	version("0.1.0", md5="826f128b5ab5fdf8368ef9741fb8fdf0")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
