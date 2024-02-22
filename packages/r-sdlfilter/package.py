# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdlfilter(RPackage):
	"""Filtering and Assessing the Sample Size of Tracking Data

	Functions to filter GPS/Argos locations, as well as assessing the sample size for the analysis of animal distributions. The filters remove temporal and spatial duplicates, fixes located at a given height from estimated high tide line, and locations with high error as described in Shimada et al. (2012) <doi:10.3354/meps09747> and Shimada et al. (2016) <doi:10.1007/s00227-015-2771-0>. Sample size for the analysis of animal distributions can be assessed by the conventional area-based approach or the alternative probability-based approach as described in Shimada et al. (2021) <doi:10.1111/2041-210X.13506>. 
	"""
	
	homepage = "https://github.com/TakahiroShimada/SDLfilter"
	cran = "SDLfilter" 

	version("2.3.3", md5="3170b88dc1470c1d706331884d488e2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
