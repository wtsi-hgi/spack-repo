# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgoogleads(RPackage):
	"""Loading Data from 'Google Ads API'

	Interface for loading data from 'Google Ads API', 
    see <https://developers.google.com/google-ads/api/docs/start>. 
    Package provide function for authorization and loading reports.
	"""
	
	homepage = "https://selesnow.github.io/rgoogleads/"
	cran = "rgoogleads" 

	version("0.10.0", md5="2f7155cb77ab6b1351841bc776499fad")

	depends_on("r-gargle@1.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
