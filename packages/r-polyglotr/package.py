# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyglotr(RPackage):
	"""Translate Text

	The goal of the this package is to provide easy methods to 
    translate pieces of text. Functions send requests to translation services online.
	"""
	
	homepage = "https://github.com/Tomeriko96/polyglotr/"
	cran = "polyglotr" 

	version("1.4.0", md5="5bacd26bf7072cfa41f881918e20d065")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
