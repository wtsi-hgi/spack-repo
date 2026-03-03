# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwfscairdas(RPackage):
	"""Southwest Fisheries Science Center Aerial DAS Data Processing

	Process and summarize aerial survey 'DAS' data (AirDAS) 
    <https://swfsc-publications.fisheries.noaa.gov/publications/TM/SWFSC/NOAA-TM-NMFS-SWFSC-185.PDF>
    collected using an aerial survey program from the 
    Southwest Fisheries Science Center (SWFSC) 
    <https://www.fisheries.noaa.gov/west-coast/science-data/california-current-marine-mammal-assessment-program>.
    PDF files detailing the relevant AirDAS data formats are included in this package.
	"""
	
	homepage = "https://smwoodman.github.io/swfscAirDAS/"
	cran = "swfscAirDAS" 

	version("0.3.0", md5="57080f8efc550b0bace1828fffe02052")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-swfscdas@0.3:", type=("build", "run"))
	depends_on("r-swfscmisc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
