# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElist(RPackage):
	"""List Comprehension and Tools

	
    Create list comprehensions (and other types of comprehension) similar to those in
    'python', 'haskell', and other languages. List comprehension in 'R' converts a 
    regular for() loop into a vectorized lapply() function. Support for looping 
    with multiple variables, parallelization, and across non-standard objects included. Package 
    also contains a variety of functions to help with list comprehension.
	"""
	
	cran = "eList" 

	version("0.2.0", md5="0dca5803ca2b648bf2602837f47c14db")

