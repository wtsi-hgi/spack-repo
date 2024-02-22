# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyterra(RPackage):
	"""'tidyverse' Methods and 'ggplot2' Helpers for 'terra' Objects

	Extension of the 'tidyverse' for 'SpatRaster' and
    'SpatVector' objects of the 'terra' package. It includes also new
    'geom_' functions that provide a convenient way of visualizing 'terra'
    objects with 'ggplot2'.
	"""
	
	homepage = "https://dieghernan.github.io/tidyterra/"
	cran = "tidyterra" 

	version("0.5.2", md5="4989a10b88b1dcc3baac934b1147792b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-terra@1.5.12:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
