# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTogglr(RPackage):
	"""'Toggl.com' Api for 'Rstudio'

	Use the <https://toggl.com> time tracker api through R.
	"""
	
	homepage = "https://github.com/ThinkR-open/togglr"
	cran = "togglr" 

	version("0.2.1", md5="1a4c397b7e5676512d06581c566fc354")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
