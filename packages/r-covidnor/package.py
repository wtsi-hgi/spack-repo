# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidnor(RPackage):
	"""Public COVID-19 Data for Norway

	Publicly available COVID-19 data for Norway cleaned and merged into one dataset, including PCR confirmed cases, tests, hospitalisation and vaccination.
	"""
	
	homepage = "https://www.csids.no/covidnor/"
	cran = "covidnor" 

	version("2023.05.18", md5="57e629fa3f616a9c7bd3bc20a731dd2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
