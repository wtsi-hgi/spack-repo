# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REssentials(RPackage):
	"""Essential Functions not Included in Base R

	Functions for converting objects to scalars (vectors of length 1) 
    and a more inclusive definition of data that can be interpreted as numbers 
    (numeric and complex alike).
	"""
	
	cran = "essentials" 

	version("0.1.0", md5="f9276c156103ad6becd1ddf9fac5c20c")

