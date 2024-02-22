# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSocialrisk(RPackage):
	"""Identifying Patient Social Risk from Administrative Health Care
Data

	Social risks are increasingly becoming a critical component of health
    care research. One of the most common ways to identify social needs is by using
    ICD-10-CM "Z-codes." This package identifies social risks using varying taxonomies
    of ICD-10-CM Z-codes from administrative health care data. The conceptual
    taxonomies come from:
    Centers for Medicare and Medicaid Services (2021) <https://www.cms.gov/files/document/zcodes-infographic.pdf>,
    Reidhead (2018) <https://web.mhanet.com/>,
    A Arons, S DeSilvey, C Fichtenberg, L Gottlieb (2018) <https://sirenetwork.ucsf.edu/tools-resources/resources/compendium-medical-terminology-codes-social-risk-factors>.
	"""
	
	homepage = "https://github.com/WYATTBENSKEN/multimorbidity"
	cran = "socialrisk" 

	version("0.5.1", md5="e4650f42930a3f9c74a5edf02aa4baee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
