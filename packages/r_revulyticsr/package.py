# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevulyticsr(RPackage):
	"""Connect to Your 'Revulytics' Data

	Facilitates making a connection to the 
  'Revulytics' API and executing various queries. You can use it to
  get event data and metadata. The Revulytics documentation 
  is available at <https://docs.revenera.com/ui560/report/>. This
  package is not supported by 'Flexera' (owner of the software). 
	"""
	
	homepage = "https://github.com/chrisumphlett/revulyticsR"
	cran = "revulyticsR" 

	version("0.0.3", md5="ed783c87cdc10f43651e005c8a39f726")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@1.0.3:", type=("build", "run"))
