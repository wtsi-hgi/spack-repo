# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNightday(RPackage):
	"""Night and Day Boundary Plot Function

	Computes and plots the boundary between night and day.
	"""
	
	cran = "NightDay" 

	version("1.0.1.1", md5="82b1cb642368cebe68a209f4b335ef91")

	depends_on("r@2.9.9:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
