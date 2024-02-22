# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNasapower(RPackage):
	"""NASA POWER API Client

	An API client for NASA POWER global meteorology, surface solar
    energy and climatology data API.  POWER (Prediction Of Worldwide Energy
    Resources) data are freely available for download with varying spatial 
    resolutions dependent on the original data and with several temporal
    resolutions depending on the POWER parameter and community.  This work is
    funded through the NASA Earth Science Directorate Applied Science Program.
    For more on the data themselves, the methodologies used in creating, a web-
    based data viewer and web access, please see <https://power.larc.nasa.gov/>.
	"""
	
	homepage = "https://docs.ropensci.org/nasapower/"
	cran = "nasapower" 

	version("4.2.0", md5="19622bbaf902c04e78081fc748e23303")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@3.0.2:", type=("build", "run"))
