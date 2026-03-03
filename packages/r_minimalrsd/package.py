# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinimalrsd(RPackage):
	"""Minimally Changed CCD and BBD

	Generate central composite designs (CCD)with full as well 
    as fractional factorial points (half replicate) and Box Behnken 
    designs (BBD) with minimally changed run sequence.
	"""
	
	cran = "minimalRSD" 

	version("1.0.0", md5="bb01bfdb1bc0ab1bfe5f9324555df661")

