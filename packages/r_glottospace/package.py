# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlottospace(RPackage):
	"""Language Mapping and Geospatial Analysis of Linguistic and
Cultural Data

	Streamlined workflows for geolinguistic analysis, including:
    accessing global linguistic and cultural databases, data import, data
    entry, data cleaning, data exploration, mapping, visualization and
    export.
	"""
	
	homepage = "https://github.com/SietzeN/glottospace"
	cran = "glottospace" 

	version("0.0.112", md5="bf8359367887a0103cb1395f0785a8ad")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-rnaturalearthdata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
