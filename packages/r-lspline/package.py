# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLspline(RPackage):
	"""Linear Splines with Convenient Parametrisations

	Linear splines with convenient parametrisations such that 
  (1) coefficients are slopes of consecutive segments or (2) coefficients are 
  slope changes at consecutive knots. Knots can be set manually or at break points
  of equal-frequency or equal-width intervals covering the range of 'x'.
  The implementation follows Greene (2003), chapter 7.2.5.
	"""
	
	cran = "lspline" 

	version("1.0-0", md5="1dfd7137450c6c39882e765761984dc0")

