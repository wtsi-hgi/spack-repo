# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSweep(RPackage):
	"""Tidy Tools for Forecasting

	
    Tidies up the forecasting modeling and prediction work flow, 
    extends the 'broom' package 
    with 'sw_tidy', 'sw_glance', 'sw_augment', and 'sw_tidy_decomp' functions 
    for various forecasting models,
    and enables converting 'forecast' objects to 
    "tidy" data frames with 'sw_sweep'.
	"""
	
	homepage = "https://github.com/business-science/sweep"
	cran = "sweep" 

	version("0.2.5", md5="42333d54e0e7f9ec220dd0ed9228b5dd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-broom@0.5.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-forecast@8:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-timetk@2.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-tidyquant", type=("build", "run"))
