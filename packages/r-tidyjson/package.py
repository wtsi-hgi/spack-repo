# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyjson(RPackage):
	"""Tidy Complex 'JSON'

	Turn complex 'JSON' data into tidy data frames.
	"""
	
	homepage = "https://github.com/colearendt/tidyjson"
	cran = "tidyjson" 

	version("0.3.2", md5="116eeb673c08f61987292eee82b23409")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
