# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdscore(RPackage):
	"""Improved Score Tests for Generalized Linear Models

	A set of functions to obtain modified score test for generalized linear models.
	"""
	
	cran = "mdscore" 

	version("0.1-3", md5="754815ad4ec718e3e9555d82b38d68d4")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
