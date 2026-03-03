# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHurricaneexposure(RPackage):
	"""Explore and Map County-Level Hurricane Exposure in the United
States

	Allows users to create time series of tropical storm
    exposure histories for chosen counties for a number of hazard metrics
    (wind, rain, distance from the storm, etc.). This package interacts
    with data available through the 'hurricaneexposuredata' package, which
    is available in a 'drat' repository. To access this data package, see the 
    instructions at <https://github.com/geanders/hurricaneexposure>. 
    The size of the 'hurricaneexposuredata' package is
    approximately 20 MB. This work was supported in part by grants from the National
    Institute of Environmental Health Sciences (R00ES022631), the National Science
    Foundation (1331399), and a NASA Applied Sciences Program/Public Health Program
    Grant (NNX09AV81G).
	"""
	
	homepage = "https://github.com/geanders/hurricaneexposure"
	cran = "hurricaneexposure" 

	version("0.1.1", md5="3a8ed6cc872dce549f09d430c18ddd4f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggmap@3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-lazyeval@0.2.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-mapproj@1.2.6:", type=("build", "run"))
	depends_on("r-maps@3.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
