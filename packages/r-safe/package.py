# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSafe(RPackage):
	"""Significance Analysis of Function and Expression

	SAFE is a resampling-based method for testing functional categories in gene expression experiments. SAFE can be applied to 2-sample and multi-class comparisons, or simple linear regressions. Other experimental designs can also be accommodated through user-defined functions.
	"""
	
	bioc = "safe"

	version("3.48.0", commit="1eee66dc72bb0a9ab8bdeae2440a4721eaa8d5c5")
	version("3.42.0", commit="eb6249c3f68676cc39d7da868d900d22b9741ec0")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
