# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntegratebs(RPackage):
	"""Integration for B-Spline

	Integrated B-spline function.
	"""
	
	cran = "IntegrateBs" 

	version("0.1.0", md5="ef522b041bda358b578e19f5c8ca5302")

	depends_on("r@3.0.2:", type=("build", "run"))
