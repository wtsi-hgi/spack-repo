# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlider(RPackage):
	"""Sliding Window Functions

	Provides type-stable rolling window functions over any R data
    type. Cumulative and expanding windows are also supported. For more
    advanced usage, an index can be used as a secondary vector that
    defines how sliding windows are to be created.
	"""
	
	homepage = "https://github.com/r-lib/slider"
	cran = "slider" 

	version("0.3.1", md5="b40d64c6dbb50a550bf8c66ceece8cc3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
	depends_on("r-warp", type=("build", "run"))
