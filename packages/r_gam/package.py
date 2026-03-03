# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGam(RPackage):
	"""Generalized Additive Models

	Functions for fitting and working with generalized
		additive models, as described in chapter 7 of "Statistical Models in S" (Chambers and Hastie (eds), 1991), and "Generalized Additive Models" (Hastie and Tibshirani, 1990).
	"""
	
	cran = "gam" 

	version("1.22-3", md5="e3a5cdfe656f7424098907c431453bc1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
