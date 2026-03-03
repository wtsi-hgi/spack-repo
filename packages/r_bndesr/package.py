# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBndesr(RPackage):
	"""Access Data from the Brazilian Development Bank (BNDES)

	Allows access to data on BNDES disbursements and contracts since 1995. The package makes it easy to import data from the bank into R.<https://www.bndes.gov.br/SiteBNDES/bndes/bndes_en>.
	"""
	
	cran = "bndesr" 

	version("1.0.3", md5="81d55adb9911f879347e302916fb568b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
