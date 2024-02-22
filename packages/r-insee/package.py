# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsee(RPackage):
	"""Tools to Easily Download Data from INSEE BDM Database

	Using embedded sdmx queries, get the data of more than 150 000 insee series from 'bdm' macroeconomic database. 
	"""
	
	homepage = "https://pyr-opendatafr.github.io/R-Insee-Data/"
	cran = "insee" 

	version("1.1.5", md5="238aefb7975062242213c210c84fd9ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
