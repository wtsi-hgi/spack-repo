# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopernicusmarine(RPackage):
	"""Search Download and Handle Data from Copernicus Marine Service
Information

	Subset and download data from EU Copernicus Marine
    Service Information: <https://data.marine.copernicus.eu>.
    Import data on the oceans physical and biogeochemical state
    from Copernicus into R without the need of external software.
	"""
	
	homepage = "https://github.com/pepijn-devries/CopernicusMarine"
	cran = "CopernicusMarine" 

	version("0.2.3", md5="302f864a604f44586667ecd92713bc83")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
