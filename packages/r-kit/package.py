# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKit(RPackage):
	"""Data Manipulation Functions Implemented in C

	Basic functions, implemented in C, for large data manipulation. Fast vectorised ifelse()/nested if()/switch() functions, psum()/pprod() functions equivalent to pmin()/pmax() plus others which are missing from base R. Most of these functions are callable at C level.
	"""
	
	cran = "kit" 

	version("0.0.16", md5="af551d3c95b2d509d6ee4bbc2545b199")

	depends_on("r@3.1:", type=("build", "run"))
