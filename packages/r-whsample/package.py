# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhsample(RPackage):
	"""Utilities for Sampling

	Interactive tools for generating random samples. Users select an
    .xlsx, .csv, or delimited .txt file with population data and are walked through selecting the
    sample type (Simple Random Sample or Stratified), the number of backups
    desired, and a "stratify_on" value (if desired). The sample size is determined
    using a normal approximation to the hypergeometric distribution based on
    Nicholson (1956) <doi:10.1214/aoms/1177728270>. An .xlsx file is created
    with the sample and key metadata for reference. It is menu-driven and lets
    users pick an output directory. See vignettes for a detailed walk-through.
	"""
	
	cran = "whSample" 

	version("0.9.6.2", md5="1f87304a5775a3460d73731387ded4ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
