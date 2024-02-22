# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiverconn(RPackage):
	"""Fragmentation and Connectivity Indices for Riverscapes

	Indices for assessing riverscape fragmentation, including the Dendritic Connectivity Index, the Population Connectivity Index, the River Fragmentation Index, the Probability of Connectivity, and the Integral Index of connectivity. For a review, see Jumani et al. (2020) <doi:10.1088/1748-9326/abcb37> and Baldan et al. (2022) <doi:10.1016/j.envsoft.2022.105470> Functions to calculate temporal indices improvement when fragmentation due to barriers is reduced are also included.
	"""
	
	homepage = "https://github.com/damianobaldan/riverconn"
	cran = "riverconn" 

	version("0.3.31", md5="7725fd26661409576c059fa75bceea5f")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dodgr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
