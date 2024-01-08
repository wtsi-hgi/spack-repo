# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RRngwell(RPackage):
	"""Toolbox for WELL Random Number Generators

	It is a dedicated package to WELL pseudo random generators, 
  which were introduced in Panneton et al. (2006), ``Improved Long-Period 
  Generators Based on Linear Recurrences Modulo 2'', see <doi:10.1145/1132973.1132974>. 
  But this package is not intended to be used directly, you are strongly __encouraged__ 
  to use the 'randtoolbox' package, which depends on this package. 
	"""
	
	cran = "rngWELL" 

	version("0.10-9", md5="30a683f8002c1aa17ca20be5ab1dcdb6")

	depends_on("r@3.0.0:", type=("build", "run"))

