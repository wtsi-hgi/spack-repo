# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZdeskr(RPackage):
	"""Connect to Your 'Zendesk' Data

	Facilitates making a connection to the 
  'Zendesk' API and executing various queries. You can use it to
  get ticket, ticket metrics, and user data. The 'Zendesk' documentation is 
  available at <https://developer.zendesk.com/rest_api
  /docs/support/introduction>. This package is not supported by 
  'Zendesk' (owner of the software).
	"""
	
	homepage = "https://github.com/chrisumphlett/zdeskR"
	cran = "zdeskR" 

	version("0.4.0", md5="ffd866f97d4b62a27fe3d9b3c112cb86")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
