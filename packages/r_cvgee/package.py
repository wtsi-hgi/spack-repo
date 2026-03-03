# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvgee(RPackage):
	"""Cross-Validated Predictions from GEE

	Calculates predictions from generalized estimating equations and internally cross-validates them using the logarithmic, quadratic and spherical proper scoring rules; Kung-Yee Liang and Scott L. Zeger (1986) <doi:10.1093/biomet/73.1.13>.
	"""
	
	homepage = "https://drizopoulos.github.io/cvGEE/"
	cran = "cvGEE" 

	version("0.3-0", md5="ef6caf0a66a63e150a25bf44fad1482d")

