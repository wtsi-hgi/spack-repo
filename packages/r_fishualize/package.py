# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishualize(RPackage):
	"""Color Palettes Based on Fish Species

	Implementation of color palettes based on fish species. 
	"""
	
	homepage = "https://github.com/nschiett/fishualize"
	cran = "fishualize" 

	version("0.2.3", md5="678c7558fdb45da07a5b88a550aabb77")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
