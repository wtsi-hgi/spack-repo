# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteoland(RPackage):
	"""Landscape Meteorology Tools

	Functions to estimate weather variables at any position of a landscape [De Caceres et al. (2018) <doi:10.1016/j.envsoft.2018.08.003>].
	"""
	
	homepage = "https://emf-creaf.github.io/meteoland/index.html"
	cran = "meteoland" 

	version("2.2.1", md5="fdffb3860883ed6a9e7ad1e50ff0d3d7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ncdfgeom", type=("build", "run"))
	depends_on("r-ncmeta", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-cubelyr", type=("build", "run"))
