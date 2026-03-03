# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidybins(RPackage):
	"""Make Tidy Bins

	Multiple ways to bin numeric columns with a tidy output. Wraps a variety of existing binning methods into one function, and includes a new method for binning by equal value, which is useful for sales data. Provides a function to automatically summarize the properties of the binned columns. 
	"""
	
	homepage = "https://github.com/Harrison4192/tidybins"
	cran = "tidybins" 

	version("0.1.0", md5="ea96095a321ba3178a3b5e60f8e66b62")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-oner", type=("build", "run"))
	depends_on("r-strex", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-framecleaner", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-badger", type=("build", "run"))
