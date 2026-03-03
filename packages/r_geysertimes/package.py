# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeysertimes(RPackage):
	"""Geyser Data from GeyserTimes.org

	Download geyser eruption and observation data from the GeyserTimes
  site (<https://geysertimes.org>) and optionally store it locally. The vignette
  shows a simple analysis of downloading, accessing, and summarizing the data.
	"""
	
	homepage = "https://github.com/geysertimes/geysertimes-r-package"
	cran = "geysertimes" 

	version("0.1.9", md5="b0380e6fecfac319e49fc5bb5fc6a418")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
