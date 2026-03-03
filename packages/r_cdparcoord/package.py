# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdparcoord(RPackage):
	"""Top Frequency-Based Parallel Coordinates

	Parallel coordinate plotting with resolutions for large data sets
 and missing values.
	"""
	
	cran = "cdparcoord" 

	version("1.0.1", md5="870ac3be08a0f20d566a247e08100bdd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-freqparcoord", type=("build", "run"))
	depends_on("r-partools", type=("build", "run"))
