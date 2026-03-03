# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJapanstat(RPackage):
	"""Tools for Easy Use of 'e-Stat' API

	Provides tools for using the API of 'e-Stat' (<https://www.e-stat.go.jp/>), a portal site for Japanese government statistics.
    Includes functions for automatic query generation, data collection and formatting.
	"""
	
	homepage = "https://github.com/UchidaMizuki/japanstat"
	cran = "japanstat" 

	version("0.1.0", md5="b70f4eed2ea89806e8b1839be05ca1a7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-pillar@1.6.4:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
	depends_on("r-stringi@1.7.5:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-vctrs@0.3.8:", type=("build", "run"))
