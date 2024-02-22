# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpmesh(RPackage):
	"""Utilities for Japanese Mesh Code

	Helpful functions for using mesh code (80km to 100m) data in Japan. Visualize mesh code using 'ggplot2' and 'leaflet', etc.
	"""
	
	homepage = "https://uribo.github.io/jpmesh/"
	cran = "jpmesh" 

	version("2.1.0", md5="5d984e391e4978981409e59f661965be")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-leaflet@1.1:", type=("build", "run"))
	depends_on("r-memoise@1.1:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.1.4:", type=("build", "run"))
	depends_on("r-sf@0.5.5:", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-units@0.5.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-vctrs@0.3.4:", type=("build", "run"))
