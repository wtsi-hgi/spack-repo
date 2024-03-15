# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetajam(RPackage):
	"""Easily Download Data and Metadata from 'DataONE'

	A set of tools to foster the development of reproducible analytical workflow by simplifying the download of data and 
    metadata from 'DataONE' (<https://www.dataone.org>) and easily importing this information into R.
	"""
	
	homepage = "https://github.com/nceas/metajam"
	cran = "metajam" 

	version("0.2.3", md5="493694d09767c8984bfeea3cca13aeec")

	depends_on("r-dataone", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-eml", type=("build", "run"))
	depends_on("r-emld", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
