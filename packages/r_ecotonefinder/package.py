# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotonefinder(RPackage):
	"""Characterising and Locating Ecotones and Communities

	Analytical methods to locate and characterise ecotones, ecosystems and environmental patchiness along ecological gradients. Methods are implemented for isolated sampling or for space/time series. It includes Detrended Correspondence Analysis (Hill & Gauch (1980) <doi:10.1007/BF00048870>), fuzzy clustering (De Cáceres et al. (2010) <doi:10.1080/01621459.1963.10500845>), biodiversity indices (Jost (2006) <doi:10.1111/j.2006.0030-1299.14714.x>), and network analyses (Epskamp et al. (2012) <doi:10.18637/jss.v048.i04>) - as well as tools to explore the number of clusters in the data. Functions to produce synthetic ecological datasets are also provided.
	"""
	
	cran = "EcotoneFinder" 

	version("0.2.3", md5="ac976dfaf6d306867753d0f83c1fe2b4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-vegclust", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
