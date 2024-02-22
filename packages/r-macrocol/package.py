# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacrocol(RPackage):
	"""Colombian Macro-Financial Time Series Generator

	This repository aims to contribute to the econometric models' production
	with Colombian data, by providing a set of web-scrapping functions 
	of some of the main macro-financial indicators. All the sources are public and
	free, but the advantage of these functions is that they directly download 
	and harmonize the information in R's environment. No need to import or download
	additional files. You only need an internet connection!
	"""
	
	homepage = "<https://github.com/pedroCabraAcela/Scrapping-Colombian-Macrodata>"
	cran = "macrocol" 

	version("0.1.0", md5="65778d9e437eb2d526976e48bff6d962")

	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
