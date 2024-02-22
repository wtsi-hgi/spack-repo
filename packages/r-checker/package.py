# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChecker(RPackage):
	"""Checks 'R' Configuration Set Up Correctly Before Class

	Checks that students have the correct version of 'R', 'R' packages,
    'RStudio' and other dependencies installed, and that the recommended 'RStudio' 
    configuration has been applied.
	"""
	
	homepage = "https://github.com/richardjtelford/checker/"
	cran = "checker" 

	version("0.1.3", md5="237a63f152a058dbe03ef3fc8468e305")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
