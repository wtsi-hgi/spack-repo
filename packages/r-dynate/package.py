# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynate(RPackage):
	"""Dynamic Aggregation Testing

	A multiple testing procedure aims to find the rare-variant association regions. When variants are rare, the single variant association test approach suffers from low power. To improve testing power, the procedure dynamically and hierarchically aggregates smaller genome regions to larger ones and performs multiple testing for disease associations with a controlled node-level false discovery rate. This method are members of the family of ancillary information assisted recursive testing introduced in Pura, Li, Chan and Xie (2021) <arXiv:1906.07757v2> and Li, Sung and Xie (2021) <arXiv:2103.11085v2>.
	"""
	
	cran = "DYNATE" 

	version("0.1", md5="01e1180ed8b8fe71adab681c4b052829")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
