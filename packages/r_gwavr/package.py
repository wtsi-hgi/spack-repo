# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwavr(RPackage):
	"""Get Water Attributes Visually in R

	Provides methods to Get Water Attributes Visually in R ('gwavr'). This allows the user to point and click on areas within the United States and get back hydrological data, e.g. flowlines, catchments, basin boundaries, comids, etc.
	"""
	
	homepage = "https://github.com/joshualerickson/gwavr/"
	cran = "gwavr" 

	version("0.2.0", md5="3b974e1295e61475102e0fea29e575f4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leaflet-extras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-nhdplustools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-elevatr", type=("build", "run"))
	depends_on("r-whitebox", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
