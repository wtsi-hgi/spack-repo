# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvctr(RPackage):
	"""Infix Functions For Vector Operations

	Vector operations between grapes: An infix-only package! The 'invctr' functions perform common and less common operations on vectors, data frames matrices and list objects:
    - Extracting a value (range), or, finding the indices of a value (range).
    - Trimming, or padding a vector with a value of your choice.
    - Simple polynomial regression.
    - Set and membership operations.
    - General check & replace function for NAs, Inf and other values.
	"""
	
	homepage = "https://github.com/FredHasselman/invctr"
	cran = "invctr" 

	version("0.2.0", md5="5c9d4d2ea240b72a7c092c3fa19591c6")

	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
