# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnstruwwel(RPackage):
	"""Detect and Parse Historic Dates

	Automatically converts language-specific verbal information, e.g., "1st half of the 19th century," to its standardized numerical counterparts, e.g., "1801-01-01/1850-12-31." It follows the recommendations of the 'MIDAS' ('Marburger Informations-, Dokumentations- und Administrations-System'), see <doi:10.11588/artdok.00003770>.
	"""
	
	homepage = "https://github.com/stefanieschneider/unstruwwel"
	cran = "unstruwwel" 

	version("0.2.0", md5="aa78a0015c2baca062c37fef9ddb69da")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
