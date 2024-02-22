# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNjira(RPackage):
	"""SQL Like Query Interface for 'Jira'

	SQL like query interface to fetch data from any 'Jira' installation. The data is fetched using 'Jira' REST API, which can be found at the following URL: <https://developer.atlassian.com/cloud/jira/platform/rest/v2>.
	"""
	
	cran = "nJira" 

	version("0.1.1", md5="580fbf339d0e08d8dcccb8a605450402")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
