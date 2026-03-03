# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStinepack(RPackage):
	"""Stineman, a Consistently Well Behaved Method of Interpolation

	A consistently well behaved method of interpolation based on piecewise rational functions using Stineman's algorithm.
	"""
	
	cran = "stinepack" 

	version("1.5", md5="57208bd2bc0f0784efa3a296c116b1d7")
	version("1.4", md5="535abfd0248ae3c4a383d91ba3884c02")

