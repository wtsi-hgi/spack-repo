# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDarksky(RPackage):
	"""Tools to Work with the 'Dark Sky' 'API'

	Provides programmatic access to the 'Dark Sky' 'API' 
    <https://darksky.net/dev/docs>, which provides current or historical global 
    weather conditions.
	"""
	
	homepage = "https://github.com/hrbrmstr/darksky"
	cran = "darksky" 

	version("1.3.0", md5="a74d58bc7734ae66cf1fdc1efe35b6ef")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
