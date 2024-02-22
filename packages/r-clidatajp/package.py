# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClidatajp(RPackage):
	"""Data from Japan Meteorological Agency

	Includes climate data from Japan Meteorological Agency ('JMA') <https://www.jma.go.jp/jma/indexe.html>.
    Can download climate data from 'JMA'. 
	"""
	
	homepage = "https://github.com/matutosi/clidatajp"
	cran = "clidatajp" 

	version("0.5.2", md5="cd421dd7f80a4e5345aa404e6d5b9c49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
