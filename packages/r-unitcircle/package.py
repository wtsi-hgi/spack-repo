# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnitcircle(RPackage):
	"""Check if Roots of a Polynomial Lie Outside the Unit Circle

	The uc.check() function checks whether the roots of a given polynomial lie outside the Unit circle. You can also easily draw an unit circle.
	"""
	
	homepage = "https://github.com/BerriJ/UnitCircle"
	cran = "UnitCircle" 

	version("0.1.3", md5="ba4258596d1d172f6b745bef08177aa3")

