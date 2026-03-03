# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssert(RPackage):
	"""Validate Function Arguments

	Lightweight validation tool for checking function arguments and 
  validating data analysis scripts. This is an alternative to stopifnot() from 
  the 'base' package  and to assert_that() from the 'assertthat' package. It 
  provides more informative error messages and facilitates debugging.
	"""
	
	homepage = "https://github.com/OlivierBinette/assert"
	cran = "assert" 

	version("1.0.1", md5="53c5a91624d1c0d03adc69eb6f87fbfe")

