# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtrek(RPackage):
	"""Data Analysis Relating to Star Trek

	Provides datasets related to the Star Trek fictional universe and functions for working with the data.
    The package also provides access to real world datasets based on the televised series and other related licensed media productions.
    It interfaces with the Star Trek API (STAPI) (<http://stapi.co/>), 
    Memory Alpha (<https://memory-alpha.fandom.com/wiki/Portal:Main>), and Memory Beta (<https://memory-beta.fandom.com/wiki/Main_Page>) 
    to retrieve data, metadata and other information relating to Star Trek.
    It also contains several local datasets covering a variety of topics. 
    The package also provides functions for working with data from other Star Trek-related 
    R data packages containing larger datasets not stored in 'rtrek'.
	"""
	
	homepage = "https://github.com/leonawicz/rtrek"
	cran = "rtrek" 

	version("0.4.0", md5="23d6ac711ca78566c4091f9262080bfd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
