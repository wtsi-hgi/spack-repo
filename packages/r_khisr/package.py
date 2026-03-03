# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKhisr(RPackage):
	"""Retrieve Data from Kenya Health Information System (KHIS)

	
    Simplify data retrieval from Kenya's health system with a powerful interface 
    for efficient data retrieval from the Kenya Health Information System 
    (KHIS)<https://hiskenya.org>. Empower researchers, analysts, and healthcare 
    professionals to access critical health data efficiently.
	"""
	
	homepage = "https://khisr.damurka.com"
	cran = "khisr" 

	version("1.0.1", md5="56948d2cf5be2ec867c29ff260e6d95d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
