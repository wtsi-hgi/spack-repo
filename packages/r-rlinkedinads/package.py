# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlinkedinads(RPackage):
	"""Load Data from 'Linkedin Advertising API'

	Get data from 'Linkedin Advertising API' <https://learn.microsoft.com/en-us/linkedin/marketing/overview?view=li-lms-2023-10>.
    You can load ad account hierarchy (accounts, users, campaign groups, campaigns and creatives) and
    also you can load ad analytics data from your 'Linkedin' Ad account.
	"""
	
	cran = "rlinkedinads" 

	version("0.2.0", md5="e46e733c53f5b491ca63c761ab703b79")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
