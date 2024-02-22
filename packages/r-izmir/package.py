# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIzmir(RPackage):
	"""R Wrapper for Izmir Municipality Open Data Portal

	Call the data wrappers for Izmir Metropolitan Municipality's Open Data Portal. This will return all datasets formatted as Excel files (.csv or .xlsx), as well as datasets that require an API key.
	"""
	
	homepage = "https://github.com/ozancanozdemir/izmir"
	cran = "izmir" 

	version("0.1.0", md5="3653d235c9568ceb39b5f92c939a809d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
