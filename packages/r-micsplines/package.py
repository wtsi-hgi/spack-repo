# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicsplines(RPackage):
	"""The Computing of Monotonic Spline Bases and Constrained
Least-Squares Estimates

	Providing C implementation for the computing of monotonic spline bases, including M-splines, I-splines, and C-splines, denoted by MIC splines. The definitions of the spline bases are described in Meyer (2008) <doi: 10.1214/08-AOAS167>. The package also provides the computing of constrained least-squares estimates when a subset of or all of the regression coefficients are constrained to be non-negative.
	"""
	
	cran = "MICsplines" 

	version("1.0", md5="2163b6d49cae0c921bd426def1049fdc")

