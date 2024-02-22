# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCft(RPackage):
	"""Climate Futures Toolbox

	Developed as a collaboration between Earth lab and the North Central Climate Adaptation Science Center to help users gain insights from available climate data. Includes tools and instructions for downloading climate data via a 'USGS' API and then organizing those data for visualization and analysis that drive insight. Web interface for 'USGS' API can be found at <http://thredds.northwestknowledge.net:8080/thredds/reacch_climate_CMIP5_aggregated_macav2_catalog.html>.
	"""
	
	homepage = "https://github.com/earthlab/cft-CRAN"
	cran = "cft" 

	version("1.0.0", md5="9d08ab5cdf037f798428028039e076f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-osmdata", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidync", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-piper", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
