# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsspchelpr(RPackage):
	"""Helper Functions for Second Primary Cancer Analyses

	A collection of helper functions for analyzing Second Primary Cancer data, 
    including functions to reshape data, to calculate patient states and analyze cancer incidence.
	"""
	
	homepage = "https://marianschmidt.github.io/msSPChelpR/"
	cran = "msSPChelpR" 

	version("0.9.1", md5="3166cd40e9ff95e4887661bb0b30e0ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidytable@0.9:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
