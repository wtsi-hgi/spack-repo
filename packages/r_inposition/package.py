# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInposition(RPackage):
	"""Inference Tests for ExPosition

	Non-parametric resampling-based inference tests for ExPosition.
	"""
	
	cran = "InPosition" 

	version("0.12.7.1", md5="a0415b0ba7ba785e5c86af27f9cf3e57")

	depends_on("r-prettygraphs@2.1.4:", type=("build", "run"))
	depends_on("r-exposition@2:", type=("build", "run"))
