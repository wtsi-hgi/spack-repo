# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresenter(RPackage):
	"""Present Data with Style

	Consists of custom wrapper functions using packages
    'openxlsx', 'flextable', and 'officer' to create highly formatted MS office friendly output of your data frames.
    These viewer friendly outputs are intended to match expectations of professional looking presentations
    in business and consulting scenarios. The functions are opinionated in the sense that they expect the input data
    frame to have certain properties in order to take advantage of the automated formatting.
	"""
	
	homepage = "https://github.com/Harrison4192/presenter"
	cran = "presenter" 

	version("0.1.2", md5="00ab9d8af7f78eae34ddaed885daa7a9")

	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-rvg", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-framecleaner", type=("build", "run"))
