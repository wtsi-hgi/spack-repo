# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19sf(RPackage):
	"""The Covid19 San Francisco Dataset

	Provides a verity of summary tables of the Covid19 cases in San Francisco. Data source: San Francisco, Department of Public Health - Population Health Division <https://datasf.org/opendata/>.
	"""
	
	homepage = "https://github.com/RamiKrispin/covid19sf"
	cran = "covid19sf" 

	version("0.1.2", md5="786a062d73bba69eb08039e6af73a107")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
