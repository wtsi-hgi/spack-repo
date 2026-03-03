# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REye(RPackage):
	"""Analysis of Eye Data

	There is no ophthalmic researcher who has not had headaches from 
    the handling of visual acuity entries. Different notations, untidy entries. 
    This shall now be a matter of the past. Eye makes it as easy as pie to work
    with VA data - easy cleaning, easy conversion between 
    Snellen, logMAR, ETDRS letters, and qualitative visual acuity 
    shall never pester you again. The eye 
    package automates the pesky task to count number of patients and eyes, 
    and can help to clean data with easy re-coding for right and left eyes. 
    It also contains functions to help reshaping eye side specific variables 
    between wide and long format. Visual acuity conversion is based on 
    Schulze-Bonsel et al. (2006) <doi:10.1167/iovs.05-0981>, 
    Gregori et al. (2010) <doi:10.1097/iae.0b013e3181d87e04>, 
    Beck et al. (2003) <doi:10.1016/s0002-9394(02)01825-1> and 
    Bach (2007) <http:michaelbach.de/sci/acuity.html>.
	"""
	
	homepage = "https://github.com/tjebo/eye"
	cran = "eye" 

	version("1.2.1", md5="9b11f6b40ca4058b95d56a84bf2d5f03")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.0.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-english@1.2.6:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-pillar@1.6.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.1:", type=("build", "run"))
