# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrappr(RPackage):
	"""A Collection of Helper and Wrapper Functions

	Helper functions to easily add functionality to functions.  The package can 
  assign functions to have an lazy evaluation allowing you to save and update the 
  arguments before and after each function call.  You can set a temporary working 
  directory within functions and wrap console messages around other functions.
	"""
	
	cran = "wrappr" 

	version("0.1.0", md5="2f8dfdbf97fb329bd6a32fac274630e0")

