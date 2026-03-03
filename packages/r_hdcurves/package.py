# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdcurves(RPackage):
	"""Hierarchical Derivative Curve Estimation

	A procedure that fits derivative curves based on a sequence of quotient differences.  In a hierarchical setting the package produces estimates of subject-specific and group-specific derivative curves.  In a non-hierarchical setting the package produces a single derivative curve.
	"""
	
	cran = "HDCurves" 

	version("0.1.2", md5="d55e2a3d3e1240fddd2502f1b404ddea")

	depends_on("r@3.5:", type=("build", "run"))
