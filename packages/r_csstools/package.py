# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsstools(RPackage):
	"""Cognitive Social Structure Tools

	A collection of tools for estimating a network from a random sample of cognitive social structure (CSS) slices. Also contains functions for evaluating a CSS in terms of various error types observed in each slice.
	"""
	
	cran = "cssTools" 

	version("1.0", md5="5ccb057812a20ef76342be16e0b7de01")

	depends_on("r-sna", type=("build", "run"))
