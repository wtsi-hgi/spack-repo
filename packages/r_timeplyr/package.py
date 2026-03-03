# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeplyr(RPackage):
	"""Fast Tidy Tools for Date and Date-Time Manipulation

	A set of fast tidy functions for wrangling, completing and
    summarising date and date-time data. It combines 'tidyverse' syntax
    with the efficiency of 'data.table' and speed of 'collapse'.
	"""
	
	cran = "timeplyr" 

	version("0.5.0", md5="17a258c386b2001d859d564c17654f99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-collapse@2:", type=("build", "run"))
	depends_on("r-cppdoubles", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lubridate@1.9:", type=("build", "run"))
	depends_on("r-pillar@1.7:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-timechange@0.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
