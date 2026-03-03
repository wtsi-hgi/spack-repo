# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpstat(RPackage):
	"""Tools for Easy Use of 'e-Stat', 'RESAS' API, Etc

	Provides tools to use API such as 'e-Stat' (<https://www.e-stat.go.jp/>), 
    the portal site for Japanese government statistics, and 
    'RESAS' (Regional Economy and Society Analyzing System, <https://resas.go.jp>). 
	"""
	
	homepage = "https://github.com/UchidaMizuki/jpstat"
	cran = "jpstat" 

	version("0.4.0", md5="929607c4201f91814fa909391e60e4f4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-navigatr@0.2:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-stickyr", type=("build", "run"))
