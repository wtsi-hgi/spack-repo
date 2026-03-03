# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgarchery(RPackage):
	"""Flexible Segment Geoms with Arrows for 'ggplot2'

	Geoms for placing arrowheads at multiple points along a segment, not just at the end; position function to shift starts and ends of arrows to avoid exactly intersecting points.
	"""
	
	homepage = "https://github.com/mdhall272/ggarchery"
	cran = "ggarchery" 

	version("0.4.3", md5="e4af27f2342401acbf73f463662681c8")
	version("0.4.2", md5="5fa3e4a36ebd5fef71495bdb9f5d1d9a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
