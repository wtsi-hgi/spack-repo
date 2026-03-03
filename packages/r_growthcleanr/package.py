# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthcleanr(RPackage):
	"""Data Cleaner for Anthropometric Measurements

	Identifies implausible anthropometric (e.g., height,
    weight) measurements in irregularly spaced longitudinal datasets, such as those from electronic health records.
	"""
	
	homepage = "https://carriedaymont.github.io/growthcleanr/index.html"
	cran = "growthcleanr" 

	version("2.2.0", md5="32566fcf6c7cc622d951265f9ce034cf")
	version("2.1.1", md5="4f6d2aa0ae9edb6cd35a7553d0580dd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r-utils@2.11:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-labelled@2.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
