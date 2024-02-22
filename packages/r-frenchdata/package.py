# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrenchdata(RPackage):
	"""Download Data Sets from Kenneth's French Finance Data Library
Site

	Download data sets from Kenneth's French finance data library site <http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>, reads all the data subsets from the file. Allows R users to collect the data as
    'tidyverse'-ready data frames.
	"""
	
	homepage = "https://nareal.github.io/frenchdata/"
	cran = "frenchdata" 

	version("0.2.0", md5="22273f38aa1d2ee6ab06e6eae921acd2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
