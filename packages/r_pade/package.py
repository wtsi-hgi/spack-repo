# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPade(RPackage):
	"""Padé Approximant Coefficients

	Given a vector of Taylor series coefficients of sufficient length
    as input, the function returns the numerator and denominator coefficients
    for the Padé approximant of appropriate order (Baker, 1975)
    <ISBN:9780120748556>.
	"""
	
	homepage = "https://github.com/aadler/Pade"
	cran = "Pade" 

	version("1.0.6", md5="93fde3ec93d92790c525ba88b43854e3")

