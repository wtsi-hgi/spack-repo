# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetools(RPackage):
	"""Macroeconomics Tools

	Provides a number of functions to facilitate the handling and production of reports using time series data.
    The package was developed to be understandable for beginners, so some functions aim to transform processes that would be
    complex into functions with a few lines. The main advantage of using the 'metools' package is the ease of producing reports and
    working with time series using a few lines of code, so the code is clean and easy to understand/maintain. 
    Learn more about the 'metools' at <https://metoolsr.wordpress.com>.
	"""
	
	homepage = "https://metoolsr.wordpress.com"
	cran = "metools" 

	version("1.0.0", md5="a0ebb13404f9b767b184d6e6c90e6b5f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
