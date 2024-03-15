# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwfscdas(RPackage):
	"""Southwest Fisheries Science Center Shipboard DAS Data Processing

	Process and summarize shipboard 
    'DAS' <https://swfsc-publications.fisheries.noaa.gov/publications/TM/SWFSC/NOAA-TM-NMFS-SWFSC-305.PDF> data
    produced by the Southwest Fisheries Science Center (SWFSC) program 'WinCruz' 
    <https://www.fisheries.noaa.gov/west-coast/science-data/california-current-marine-mammal-assessment-program>.
    This package standardizes and streamlines basic DAS data processing,
    and includes a PDF with the DAS data format requirements.
	"""
	
	homepage = "https://smwoodman.github.io/swfscDAS/"
	cran = "swfscDAS" 

	version("0.6.2", md5="b779f40904622ecb17ced2374cab5bb3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-swfscmisc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
