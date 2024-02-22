# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchor(RPackage):
	"""Access EPA 'ECHO' Data

	An R interface to United States Environmental 
    Protection Agency (EPA) Environmental Compliance 
    History Online ('ECHO') Application Program Interface
    (API). 'ECHO' provides information about EPA permitted 
    facilities, discharges, and other reporting info 
    associated with permitted entities. Data are obtained 
    from <https://echo.epa.gov/>. 
	"""
	
	homepage = "https://github.com/mps9506/echor"
	cran = "echor" 

	version("0.1.9", md5="b912a852a0081e7b01ca31ef771c3096")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
