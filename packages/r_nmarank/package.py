# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmarank(RPackage):
	"""Complex Hierarchy Questions in Network Meta-Analysis

	Derives the most frequent hierarchies along with their probability of occurrence. One can also define complex hierarchy criteria and calculate their probability. Methodology based on Papakonstantinou et al. (2021) <DOI:10.21203/rs.3.rs-858140/v1>.
	"""
	
	homepage = "https://github.com/tpapak/nmarank"
	cran = "nmarank" 

	version("0.3-0", md5="6ca36132b2f9f1370134ed6a1902a24f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-netmeta@2.7.0:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
