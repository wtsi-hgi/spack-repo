# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwebstat(RPackage):
	"""Download Data from the Webstat API

	Access the Webstat API, download data and metadata from more than 35000 time series
    from the Banque de France statistics web portal. Access requires a free client ID easily available
    from the API portal <https://developer.webstat.banque-france.fr/>.
	"""
	
	homepage = "https://developer.webstat.banque-france.fr"
	cran = "rwebstat" 

	version("1.1.1", md5="29473e3bc7f0035032c9fea8cf57351f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
