# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBulkreadr(RPackage):
	"""The Ultimate Tool for Reading Data in Bulk

	Designed to simplify and streamline the process of reading
    and processing large volumes of data in R, this package offers a
    collection of functions tailored for bulk data operations. It enables
    users to efficiently read multiple sheets from Microsoft Excel and
    Google Sheets workbooks, as well as various CSV files from a
    directory. The data is returned as organized data frames, facilitating
    further analysis and manipulation. Ideal for handling extensive data
    sets or batch processing tasks, bulkreadr empowers users to manage
    data in bulk effortlessly, saving time and effort in data preparation
    workflows. Additionally, the package seamlessly works with labelled
    data from SPSS and Stata.
	"""
	
	homepage = "https://github.com/gbganalyst/bulkreadr"
	cran = "bulkreadr" 

	version("1.1.0", md5="f683333a35daddc742cbf1ef65778a93")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-googlesheets4", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-inspectdf", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
