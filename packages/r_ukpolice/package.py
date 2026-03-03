# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkpolice(RPackage):
	"""Download Data on UK Police and Crime

	Downloads data from the 'UK Police' public data API, 
    the full docs of which are available at <https://data.police.uk/docs/>. 
    Includes data on police forces and police force areas, crime reports, 
    and the use of stop-and-search powers.
	"""
	
	homepage = "https://github.com/EvanOdell/ukpolice/"
	cran = "ukpolice" 

	version("0.2.2", md5="50f75982aa2f1896afe037219e5248c4")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
