# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeiv(RPackage):
	"""Bivariate Linear Errors-In-Variables Estimation

	Estimate the slope and intercept of a bivariate
	linear relationship by calculating a posterior density
	that is invariant to interchange and scaling of the
	coordinates.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "leiv" 

	version("2.0-7", md5="c2154bd2234822a7e61ce7cfa00a90bc")

	depends_on("r@2.9:", type=("build", "run"))
