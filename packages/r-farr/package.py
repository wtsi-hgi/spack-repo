# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarr(RPackage):
	"""Data and Code for Financial Accounting Research

	Handy functions and data to support a course book for accounting research. 
    Gow, Ian and Tongqing Ding (2022) 'Accounting Research: An Introductory Course' <https://iangow.github.io/far_book/>.
	"""
	
	homepage = "https://github.com/iangow/farr"
	cran = "farr" 

	version("0.3.0", md5="377824e3242100723f79a3b0204db6eb")
	version("0.2.39", md5="7f49896d030777b171715241230de4ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbplyr@2.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
