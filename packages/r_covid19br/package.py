# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19br(RPackage):
	"""Brazilian COVID-19 Pandemic Data

	Set of functions to import COVID-19 pandemic data into R. The Brazilian COVID-19 data, obtained from the official Brazilian repository at <https://covid.saude.gov.br/>, is available at country, region, state, and city-levels. The package also downloads the world-level COVID-19 data from the John Hopkins University's repository.
	"""
	
	homepage = "https://fndemarqui.github.io/covid19br/"
	cran = "covid19br" 

	version("0.1.8", md5="3e8936f19c48eb05d0c6bcd10cd29936")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
