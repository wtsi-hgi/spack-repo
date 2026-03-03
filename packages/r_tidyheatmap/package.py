# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyheatmap(RPackage):
	"""A Tidy Implementation of Heatmap

	This is a tidy implementation for heatmap.  At the
    moment it is based on the (great) package 'ComplexHeatmap'.  The goal
    of this package is to interface a tidy data frame with this powerful
    tool.  Some of the advantages are: Row and/or columns colour
    annotations are easy to integrate just specifying one parameter
    (column names).  Custom grouping of rows is easy to specify providing
    a grouped tbl. For example: df %>% group_by(...).  Labels size
    adjusted by row and column total number.  Default use of Brewer and
    Viridis palettes.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "tidyHeatmap" 

	version("1.8.1", md5="043abb0854964eceb2fccc711ae64a35")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-complexheatmap@2.2:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-circlize@0.4.8:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
