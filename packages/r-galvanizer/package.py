# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGalvanizer(RPackage):
	"""Interface to Galvanize 'Highbond' Internal Audit Software

	An R interface to the Galvanize 'Highbond' API <https://docs-apis.highbond.com>.
	"""
	
	homepage = "https://jonlinca.github.io/galvanizer/"
	cran = "galvanizer" 

	version("0.5.3", md5="8a8fd7ae8a75e5260614c325cdaadddb")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyjson", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
