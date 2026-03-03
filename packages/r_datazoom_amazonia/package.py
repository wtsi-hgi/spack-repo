# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatazoomAmazonia(RPackage):
	"""Simplify Access to Data from the Amazon Region

	Functions to download and treat data regarding the Brazilian
    Amazon region from a variety of official sources.
	"""
	
	homepage = "https://www.econ.puc-rio.br/datazoom/"
	cran = "datazoom.amazonia" 

	version("1.1.0", md5="8555ff213627f7959b29f753f8219422")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sidrar", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
