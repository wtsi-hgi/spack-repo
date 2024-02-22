# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxskew(RPackage):
	"""Orthogonal Data Projections with Maximal Skewness

	It finds Orthogonal Data Projections with Maximal Skewness. The first data projection in the output is the most skewed among all linear data projections. The second data projection in the output is the most skewed among all data projections orthogonal to the first one, and so on. 
	"""
	
	cran = "MaxSkew" 

	version("1.1", md5="0b2992814968f4c190123233fc92f63d")

