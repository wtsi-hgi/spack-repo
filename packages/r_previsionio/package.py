# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevisionio(RPackage):
	"""'Prevision.io' R SDK

	For working with the 'Prevision.io' AI model management platform's API <https://prevision.io/>.
	"""
	
	cran = "previsionio" 

	version("11.7.0", md5="463b6854cc6ca711d203d30f6e57e234")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
