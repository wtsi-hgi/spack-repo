# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatadictionary(RPackage):
	"""Create a Data Dictionary

	Creates a data dictionary from any dataframe or tibble in your R environment. 
    You can opt to add variable labels. You can write the object directly to Excel.
	"""
	
	cran = "datadictionary" 

	version("1.0.0", md5="f4f12db9c64fd8cfe7f84c0c99915ce7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
