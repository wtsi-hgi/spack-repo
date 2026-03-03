# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRb3(RPackage):
	"""Download and Parse Public Data Released by B3 Exchange

	Download and parse public files released by B3 and convert them
    into useful formats and data structures common to data analysis
    practitioners.
	"""
	
	homepage = "https://github.com/ropensci/rb3"
	cran = "rb3" 

	version("0.0.10", md5="611ec55cddb0d4a5a09fe844ab191666", url="https://cran.r-project.org/src/contrib/rb3_0.0.10.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-bizdays", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-proto", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ascii", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
