# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrack2kba(RPackage):
	"""Identifying Important Areas from Animal Tracking Data

	Functions for preparing and analyzing animal tracking data, 
    with the intention of identifying areas which are potentially important at 
    the population level and therefore of conservation interest. Areas identified 
    using this package may be checked against global or regionally-defined criteria,
    such as those set by the Key Biodiversity Area program. The method
    published herein is described in full in Beal et al. 2021 <doi:10.1111/2041-210X.13713>.
	"""
	
	homepage = "https://github.com/BirdLifeInternational/track2kba"
	cran = "track2KBA" 

	version("1.1.1", md5="8cfe53b2e1363de62b1e46ab63ffb798")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-adehabitathr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-matching", type=("build", "run"))
	depends_on("r-move", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-raster@3.6.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf@0.7.4:", type=("build", "run"))
	depends_on("r-sp@1.5.0:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
