# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgnc(RPackage):
	"""Download and Import the HUGO Gene Nomenclature Committee
('HGNC') Data Set into R

	A set of routines to quickly download and import the 'HGNC'
    data set on mapping of gene symbols to gene entries in other popular
    databases or resources.
	"""
	
	homepage = "https://github.com/ramiromagno/hgnc"
	cran = "hgnc" 

	version("0.1.4", md5="ea2661263b583d80db43083fffa9ae77")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
