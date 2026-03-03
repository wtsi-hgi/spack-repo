# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatadogr(RPackage):
	"""R Client for 'Datadog' API

	Query for metrics from 'Datadog' (<https://www.datadoghq.com/>) via its API.
	"""
	
	homepage = "https://yutannihilation.github.io/K9"
	cran = "datadogr" 

	version("0.1.2", md5="fc5d97e334b52f275a4613f4f7d7caf3")

	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
