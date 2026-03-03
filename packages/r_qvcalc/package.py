# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQvcalc(RPackage):
	"""Quasi Variances for Factor Effects in Statistical Models

	Functions to compute quasi variances and associated measures of approximation error.
	"""
	
	homepage = "https://davidfirth.github.io/qvcalc/"
	cran = "qvcalc" 

	version("1.0.3", md5="2494a818e5a13b2d8b4b7f6c7e3fe8bb")

