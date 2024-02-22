# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDssat(RPackage):
	"""A Comprehensive R Interface for the DSSAT Cropping Systems Model

	The purpose of this package is to provide a comprehensive
    R interface to the Decision Support System for Agrotechnology
    Transfer Cropping Systems Model (DSSAT-CSM; see <https://dssat.net> for more information).
    The package provides cross-platform functions to read and
    write input files, run DSSAT-CSM, and read output files.
	"""
	
	cran = "DSSAT" 

	version("0.0.9", md5="6bec3adeb2052ca05672dae5dd6924bd")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
