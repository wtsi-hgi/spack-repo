# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemiestimate(RPackage):
	"""Solve Semi-Parametric Estimation by Implicit Profiling

	Semi-parametric estimation problem can be solved by two-step Newton-Raphson iteration. The implicit profiling method<arXiv:2108.07928> is an improved method of two-step NR iteration especially for the implicit-bundled type of the parametric part and non-parametric part. This package provides a function semislv() supporting the above two methods and numeric derivative approximation for unprovided Jacobian matrix.
	"""
	
	cran = "SemiEstimate" 

	version("1.1.3", md5="e70e93c120e3d57ebffade1ed7d0503d")

