# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgoutlier(RPackage):
	"""Identify Individuals with Unusual Geo-Genetic Patterns

	Identify and visualize individuals with unusual association patterns of genetics and geography using the approach of Chang and Schmid (2023) <doi:10.1101/2023.04.06.535838>. It detects potential outliers that violate the isolation-by-distance assumption using the K-nearest neighbor approach. You can obtain a table of outliers with statistics and visualize unusual geo-genetic patterns on a geographical map. This is useful for landscape genomics studies to discover individuals with unusual geography and genetics associations from a large biological sample.
	"""
	
	cran = "GGoutlieR" 

	version("1.0.2", md5="36f89e9b484a1cbb66242e48d5db6b57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastknn", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
