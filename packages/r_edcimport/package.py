# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdcimport(RPackage):
	"""Import Data from EDC Software

	A convenient toolbox to import data exported from Electronic Data Capture (EDC) software 'TrialMaster'.
	"""
	
	homepage = "https://github.com/DanChaltiel/EDCimport"
	cran = "EDCimport" 

	version("0.4.1", md5="ef52def18aa946fe750e8db91b670578")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
