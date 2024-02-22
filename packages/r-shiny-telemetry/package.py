# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyTelemetry(RPackage):
	"""'Shiny' App Usage Telemetry

	Enables instrumentation of 'Shiny' apps for tracking user
    session events such as input changes, browser type, and session
    duration.  These events can be sent to any of the available storage
    backends and analyzed using the included 'Shiny' app to gain insights
    about app usage and adoption.
	"""
	
	homepage = "https://appsilon.github.io/shiny.telemetry/"
	cran = "shiny.telemetry" 

	version("0.2.0", md5="227d6d0dfe79b3f91b9a578cd49aa60d")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
