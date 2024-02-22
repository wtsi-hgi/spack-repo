# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNullabor(RPackage):
	"""Tools for Graphical Inference

	Tools for visual inference. Generate null data sets
    and null plots using permutation and simulation. Calculate distance metrics
    for a lineup, and examine the distributions of metrics.
	"""
	
	homepage = "http://github.com/dicook/nullabor"
	cran = "nullabor" 

	version("0.3.9", md5="af27bdeb3d6a4da6ec101f5592ff13cb")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-tsibble", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
