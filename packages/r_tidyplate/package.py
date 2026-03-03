# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyplate(RPackage):
	"""Transform Microplate Data into Tidy Dataframes

	The goal of 'tidyplate' is to help researchers convert different types of
    microplates into tidy dataframes which can be used in data analysis. It accepts xlsx and
    csv files formatted in a specific way as input. It supports all types of 
    standard microplate formats such as 6-well, 12-well, 24-well, 48-well, 96-well, 384-well,
    and, 1536-well plates.
	"""
	
	homepage = "https://github.com/shubhamdutta26/tidyplate"
	cran = "tidyplate" 

	version("1.1.0", md5="eaccac59dc8a9f06ee02ad519c2fedef")

	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
