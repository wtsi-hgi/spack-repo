# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsankeyfier(RPackage):
	"""Create Sankey and Alluvial Diagrams Using 'ggplot2'

	Sankey and alluvial diagrams visualise flows of quantities across
    stages in stacked bars. This package makes it easy to create such
    diagrams using 'ggplot2'.
	"""
	
	homepage = "https://pepijn-devries.github.io/ggsankeyfier/"
	cran = "ggsankeyfier" 

	version("0.1.7", md5="d4878b1864506ce25cf6346df84d871f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-gridbezier", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vwline", type=("build", "run"))
