# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REph(RPackage):
	"""Argentina's Permanent Household Survey Data and Manipulation
Utilities

	Tools to download and manipulate the Permanent Household Survey from Argentina
    (EPH is the Spanish acronym for Permanent Household Survey).
    e.g: get_microdata() for downloading the datasets, get_poverty_lines() for downloading the official poverty baskets,
    calculate_poverty() for the calculation of stating if a household is in poverty or not, following the official methodology.
    organize_panels() is used to concatenate observations from different periods, and organize_labels()
    adds the official labels to the data. The implemented methods are based on INDEC (2016) <http://www.estadistica.ec.gba.gov.ar/dpe/images/SOCIEDAD/EPH_metodologia_22_pobreza.pdf>.
    As this package works with the argentinian Permanent Household Survey and its main audience is from this country,
    the documentation was written in Spanish.
	"""
	
	homepage = "https://github.com/holatam/eph"
	cran = "eph" 

	version("1.0.0", md5="c554b03ec108091074b9aac5ff94f3ec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-expss", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
