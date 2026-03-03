# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQbr(RPackage):
	"""Access the 'Quickbase' JSON API

	Programmatically access the 'Quickbase' JSON API <https://developer.quickbase.com>. 
    You supply parameters for an API call, 'qbr' delivers an http request to the 
    API endpoint and returns its response. Outputs follow 'tidyverse' philosophy.
	"""
	
	homepage = "https://github.com/BHII-KSC/qbr"
	cran = "qbr" 

	version("1.2.3", md5="0c91687961fcfea87ecae9ab44e8bc43")

	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
