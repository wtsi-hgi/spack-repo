# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRytstat(RPackage):
	"""Work with 'YouTube API'

	Provide function for get data from 'YouTube Data API' 
    <https://developers.google.com/youtube/v3/docs/>, 'YouTube Analytics API' 
    <https://developers.google.com/youtube/analytics/reference/> and 
    'YouTube Reporting API' <https://developers.google.com/youtube/reporting/v1/reports>.
	"""
	
	homepage = "https://selesnow.github.io/rytstat/docs/"
	cran = "rytstat" 

	version("0.3.0", md5="0621d41cdf2971cb065f6767182278f5")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gargle", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
