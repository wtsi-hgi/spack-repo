# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimaemet(RPackage):
	"""Climate AEMET Tools

	Tools to download the climatic data of the Spanish
    Meteorological Agency (AEMET) directly from R using their API and
    create scientific graphs (climate charts, trend analysis of climate
    time series, temperature and precipitation anomalies maps, warming
    stripes graphics, climatograms, etc.).
	"""
	
	homepage = "https://ropenspain.github.io/climaemet/"
	cran = "climaemet" 

	version("1.2.1", md5="2b5f34b28265aff8d644b37d75402821")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
