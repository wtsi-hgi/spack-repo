# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFude(RPackage):
	"""Utilities for Fude Polygon

	Provides utilities to facilitate handling of Fude Polygon data 
    downloadable from the Ministry of Agriculture, Forestry and Fisheries 
    website <https://open.fude.maff.go.jp>.
	"""
	
	homepage = "https://github.com/takeshinishimura/fude"
	cran = "fude" 

	version("0.3.5", md5="8cec651558605ed06464d040523113b9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
