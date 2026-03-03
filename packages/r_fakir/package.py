# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFakir(RPackage):
	"""Generate Fake Datasets for Prototyping and Teaching

	Create fake datasets that can be used for prototyping and teaching.
    This package provides a set of functions to generate fake data
    for a variety of data types, such as dates, addresses,
    and names. It can be used for prototyping (notably in 'shiny') or as a tool
    to teach data manipulation and data visualization.
	"""
	
	homepage = "https://github.com/Thinkr-open/fakir"
	cran = "fakir" 

	version("1.0.0", md5="d983611824eb816485dd01e4c4fd4872")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
	depends_on("r-charlatan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
