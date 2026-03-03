# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilterjsats(RPackage):
	"""Filter Raw JSATS Acoustic Telemetry Files from Lotek, ATS,
Teknologic

	Filtering of raw acoustic telemetry transmissions
    from three acoustic telemetry companies (ATS, Lotek, Teknologic). The 
    filtering steps check for false positives caused by reflected transmissions 
    from surfaces and false pings from other noise generating equipment. The 
    filter is unique for each technology type. The package was written in 
    concert with the Interagency Telemetry Advisory Group (iTAG) and makes use 
    of the JSATS California Fish Tracking Database:
    <https://oceanview.pfeg.noaa.gov/CalFishTrack/>.
	"""
	
	cran = "filteRjsats" 

	version("1.0", md5="80ec83e7d7e4dc723baf5c16df33d4b1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-broman", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rerddap", type=("build", "run"))
