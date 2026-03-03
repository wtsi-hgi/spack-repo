# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValhallr(RPackage):
	"""A Tidy Interface to the 'Valhalla' Routing Engine

	An interface to the 'Valhalla' routing engine’s
    application programming interfaces (APIs) for turn-by-turn routing,
    isochrones, and origin-destination analyses. Also includes several
    user-friendly functions for plotting outputs, and strives to follow
    "tidy" design principles. Please note that this package requires
    access to a running instance of 'Valhalla', which is open source and
    can be downloaded from <https://github.com/valhalla/valhalla>.
	"""
	
	homepage = "https://github.com/chris31415926535/valhallr"
	cran = "valhallr" 

	version("0.1.0", md5="29600dc7fba5a44d6d5b9d4ec26552e3")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-geojsonio", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
