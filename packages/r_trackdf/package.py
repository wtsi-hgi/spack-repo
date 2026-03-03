# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrackdf(RPackage):
	"""Data Frame Class for Tracking Data

	Data frame class for storing collective movement data (e.g. fish
    schools, ungulate herds, baboon troops) collected from GPS trackers or 
    computer vision tracking software. 
	"""
	
	homepage = "https://swarm-lab.github.io/trackdf/"
	cran = "trackdf" 

	version("0.3.3", md5="3f7ab33bc152d1b07c38df20f8cd8116")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
