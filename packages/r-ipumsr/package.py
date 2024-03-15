# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpumsr(RPackage):
	"""An R Interface for Downloading, Reading, and Handling IPUMS Data

	An easy way to work with census, survey, and geographic data
    provided by IPUMS in R. Generate and download data through the IPUMS
    API and load IPUMS files into R with their associated metadata to
    make analysis easier. IPUMS data describing 1.4 billion individuals
    drawn from over 750 censuses and surveys is available free of charge
    from the IPUMS website <https://www.ipums.org>.
	"""
	
	homepage = "https://tech.popdata.org/ipumsr/"
	cran = "ipumsr" 

	version("0.7.2", md5="8cfd41360fffd1842c921f9d8af5e40f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-haven@2.2:", type=("build", "run"))
	depends_on("r-hipread@0.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
