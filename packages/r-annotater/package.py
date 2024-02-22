# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotater(RPackage):
	"""Annotate Package Load Calls

	Provides non-invasive annotation of package load calls 
    such as code{library()}, code{p_load()}, and code{require()} so that we can have an idea of what 
    the packages we are loading are meant for.
	"""
	
	homepage = "https://github.com/luisDVA/annotater"
	cran = "annotater" 

	version("0.2.3", md5="6548e54c0ca39569dfc68b72916f3db9")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
