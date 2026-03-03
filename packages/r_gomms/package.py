# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGomms(RPackage):
	"""GLM-Based Ordination Method

	A zero-inflated quasi-Poisson factor model to display similarity between samples visually in a low (2 or 3) dimensional space.
	"""
	
	cran = "gomms" 

	version("1.0", md5="841c0084059c27bfe451d96eb48543e5")

