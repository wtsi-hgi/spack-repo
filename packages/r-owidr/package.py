# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwidr(RPackage):
	"""Import Data from Our World in Data

	Import data from 'Our World in Data', an organisation which publishes research and data on global economic and social issues.
	"""
	
	homepage = "<https://github.com/piersyork/owidR>"
	cran = "owidR" 

	version("1.4.2", md5="b5b2d9bb50665a7f57a94c698a0fd1d2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
