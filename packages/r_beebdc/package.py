# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeebdc(RPackage):
	"""Occurrence Data Cleaning

	Flags and checks occurrence data that are in Darwin Core
    format.  The package includes generic functions and data as well as
    some that are specific to bees. This package is meant to build upon
    and be complimentary to other excellent occurrence cleaning packages,
    including 'bdc' and 'CoordinateCleaner'.  This package uses datasets
    from several sources and particularly from the Discover Life Website,
    created by Ascher and Pickering (2020).  For further information,
    please see the original publication and package website.  Publication
    - Dorey et al. (2023) <doi:10.1101/2023.06.30.547152> and package
    website - Dorey et al. (2023) <https://github.com/jbdorey/BeeBDC>.
	"""
	
	cran = "BeeBDC" 

	version("1.1.0", md5="4d54b743626ac05cd00eb315dba0393f")
	version("1.0.4", md5="8d3cefd9b26e1aabf4fca1197384d4b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-coordinatecleaner", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mgsub", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
