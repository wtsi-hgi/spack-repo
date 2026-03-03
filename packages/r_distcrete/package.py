# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistcrete(RPackage):
	"""Discrete Distribution Approximations

	Creates discretised versions of continuous 
      distribution functions by mapping continuous values 
      to an underlying discrete grid, based on a (uniform) 
      frequency of discretisation, a valid discretisation 
      point, and an integration range. For a review of 
      discretisation methods, see 
      Chakraborty (2015) <doi:10.1186/s40488-015-0028-6>.
	"""
	
	homepage = "https://github.com/reconhub/distcrete"
	cran = "distcrete" 

	version("1.0.3", md5="09e26b59122d32fc479697c54f3624ec")

