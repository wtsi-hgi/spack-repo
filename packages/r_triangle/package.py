# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriangle(RPackage):
	"""Distribution Functions and Parameter Estimates for the Triangle
Distribution

	Provides the "r, q, p, and d" distribution functions for the triangle distribution.  Also includes maximum likelihood estimation of parameters.
	"""
	
	homepage = "https://bertcarnell.github.io/triangle/"
	cran = "triangle" 

	version("1.0", md5="a2dd80e5181a3b025ea2d4c258ea9955")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
