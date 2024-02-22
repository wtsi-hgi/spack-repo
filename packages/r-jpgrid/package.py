# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpgrid(RPackage):
	"""Functions for the Grid Square Codes in Japan

	Provides functions for grid square codes in Japan
    (<https://www.stat.go.jp/english/data/mesh/index.html>).
    Generates the grid square codes from longitude/latitude, geometries, and 
    the grid square codes of different scales, and vice versa.
	"""
	
	homepage = "https://github.com/UchidaMizuki/jpgrid"
	cran = "jpgrid" 

	version("0.3.1", md5="64e87aedbf2cb18fa036ccb620dafcea")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
