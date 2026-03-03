# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeonplantecology(RPackage):
	"""Process NEON Plant Data for Ecological Analysis

	Downloading and organizing plant presence and percent cover data from the National Ecological Observatory Network <https://www.neonscience.org>.
	"""
	
	homepage = "https://github.com/admahood/neonPlantEcology"
	cran = "neonPlantEcology" 

	version("1.5.0", md5="f9a1728f59902b96be2220e198fdc681")
	version("1.4.0", md5="e5e12948a0aa4cbd53c0dcb6eb777475")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-neonutilities", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dtplyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
