# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBfs(RPackage):
	"""Get Data from the Swiss Federal Statistical Office

	Search and download data from the Swiss Federal Statistical Office (BFS) APIs <https://www.bfs.admin.ch/>.
	"""
	
	homepage = "https://felixluginbuhl.com/BFS/"
	cran = "BFS" 

	version("0.5.8", md5="8b82b5d923ba0fdc1104216171751d54")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pxweb", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-tidyrss", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rstac", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
