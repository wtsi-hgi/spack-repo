# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreesixtygiving(RPackage):
	"""Download Charitable Grants from the '360Giving' Platform

	Access open data from <https://www.threesixtygiving.org>, a 
    database of charitable grant giving in the UK operated by '360Giving'.
    The package provides functions to search and retrieve data on charitable 
    grant giving, and process that data into tidy formats. It relies on the 
    '360Giving' data standard, described at 
    <https://standard.threesixtygiving.org/>.
	"""
	
	homepage = "https://docs.evanodell.com/threesixtygiving"
	cran = "threesixtygiving" 

	version("0.2.2", md5="dddf5ad0c7289c3b5a93e399f1837d61")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
