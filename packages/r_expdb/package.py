# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpdb(RPackage):
	"""Database for Experiment Dataset

	A SQLite database is designed to store all information 
  of experiment-based data including metadata, experiment design, 
  managements, phenotypic values and climate records. The dataset can be
  imported from an excel file.
	"""
	
	homepage = "https://expdb.bangyou.me/"
	cran = "expDB" 

	version("0.1.0", md5="26117ecac22147e35fffe2da4a49fe20")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-weaana@0.1.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
