# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSipdibge(RPackage):
	"""Collection of Household Survey Packages Conducted by IBGE

	Provides access to packages developed for downloading, reading and analyzing
  microdata from household surveys in Integrated System of Household Surveys - SIPD
  conducted by Brazilian Institute of Geography and Statistics - IBGE.
	More information can be obtained from the official website <https://www.ibge.gov.br/>.
	"""
	
	cran = "SIPDIBGE" 

	version("0.2.1", md5="12a4029a8ede21775ee9163cba043884")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-covidibge@0.1:", type=("build", "run"))
	depends_on("r-pnadcibge@0.6:", type=("build", "run"))
	depends_on("r-pndsibge@0.1:", type=("build", "run"))
	depends_on("r-pnsibge@0.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
