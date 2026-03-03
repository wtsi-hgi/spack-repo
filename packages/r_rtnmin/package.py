# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtnmin(RPackage):
	"""Truncated Newton Function Minimization with Bounds Constraints

	Truncated Newton function minimization with bounds constraints
	based on the 'Matlab'/'Octave' codes of Stephen Nash.
	"""
	
	cran = "Rtnmin" 

	version("2016-7.7", md5="8602bcbd65b7657dc3a4d1387abff472")

