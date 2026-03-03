# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrqol(RPackage):
	"""Minimal Clinically Important Difference and Response Shift
Effect for Health-Related Quality of Life

	We can calculate directly used this package the Minimal Clinically Important Difference by applying the Anchor-based method and the Response shift effect by applying the Then-Test method.
	"""
	
	cran = "MRQoL" 

	version("1.0", md5="d492e54998bef4eeb42099cf0183f574")

