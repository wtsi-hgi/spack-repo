# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpeadatar(RPackage):
	"""API Wrapper for 'Ipeadata'

	Allows direct access to the macroeconomic, 
             financial and regional database maintained by 
             Brazilian Institute for Applied Economic Research ('Ipea').
             This R package uses the 'Ipeadata' API. For more information, 
             see <http://www.ipeadata.gov.br/>.
	"""
	
	homepage = "https://github.com/gomesleduardo/ipeadatar"
	cran = "ipeadatar" 

	version("0.1.6", md5="ea12ed640e995f6133d0d60b9a0cb709")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
