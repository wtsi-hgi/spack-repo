# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerhoeff(RPackage):
	"""Implementation of the 'Verhoeff' Check Digit Algorithm

	An implementation of the 'Verhoeff' algorithm for calculating 
    check digits (Verhoeff, J. (1969) <doi:10.1002/zamm.19710510323>). 
    Functions are provided to calculate a check digit given an input number, 
    calculate and append a check digit to an input number, and validate that a 
    check digit is correct given an input number.
	"""
	
	cran = "verhoeff" 

	version("0.4.0", md5="3da49f31341fc29043034d236a9a4507")

