# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdherencerx(RPackage):
	"""Assess Medication Adherence from Pharmaceutical Claims Data

	A (mildly) opinionated set of functions to help assess medication adherence for researchers working with medication claims data.
    Medication adherence analyses have several complex steps that are often convoluted and can be time-intensive. The focus is to create a 
    set of functions using "tidy principles" geared towards transparency, speed, and flexibility while working with adherence metrics. All functions perform exactly one task 
    with an intuitive name so that a researcher can handle details (often achieved with vectorized solutions) while we handle non-vectorized tasks common to most 
    adherence calculations such as adjusting fill dates and determining episodes of care. The methodologies in referenced in this package come from
    Canfield SL, et al (2019) "Navigating the Wild West of Medication Adherence Reporting in Specialty Pharmacy" <doi:10.18553/jmcp.2019.25.10.1073>.
	"""
	
	homepage = "https://github.com/btbeal/adheRenceRX"
	cran = "adheRenceRX" 

	version("1.0.0", md5="ae1fdc876aab25cb74bd922399860827")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
