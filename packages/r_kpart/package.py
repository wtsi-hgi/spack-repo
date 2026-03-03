# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKpart(RPackage):
	"""Cubic Spline Fitting with Knot Selection

	Cubic spline fitting along with knot selection, includes support for additional variables.
	"""
	
	cran = "Kpart" 

	version("1.2.2", md5="9ce208b608df423bc4acec0b0c000ecd")

	depends_on("r-leaps", type=("build", "run"))
