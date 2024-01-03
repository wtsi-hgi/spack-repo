# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RLocfdr(RPackage):
	"""Computes Local False Discovery Rates

	Computation of local false discovery rates.
	"""
	
	cran = "locfdr" 

	version("1.1-8", md5="d4ee3349e9cb39b70bfff94ff665d2aa")


