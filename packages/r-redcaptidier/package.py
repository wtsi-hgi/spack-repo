# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcaptidier(RPackage):
	"""Extract 'REDCap' Databases into Tidy 'Tibble's

	Convert 'REDCap' exports into tidy tables for easy handling of 'REDCap' repeat instruments and event arms.
	"""
	
	homepage = "https://chop-cgtinformatics.github.io/REDCapTidieR/"
	cran = "REDCapTidieR" 

	version("1.0.0", md5="e427e94caee53c494bf295047a47a51e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-redcapr@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
