# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVagalumer(RPackage):
	"""Access to the 'Vagalume' API

	Provides access to the 'Vagalume' API <https://api.vagalume.com.br>. 
    The data extracted is basically lyrics of songs and information about
    artists/bands.
	"""
	
	homepage = "https://github.com/r-music/vagalumeR"
	cran = "vagalumeR" 

	version("0.1.6", md5="d29f3f9e5f62f5cf3b217e627f8b6c61")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
