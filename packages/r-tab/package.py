# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTab(RPackage):
	"""Create Summary Tables for Statistical Reports

	Contains functions for creating various types of summary tables, e.g. comparing characteristics across levels of a categorical variable and summarizing fitted generalized linear models, generalized estimating equations, and Cox proportional hazards models. Functions are available to handle data from simple random samples as well as complex surveys.
	"""
	
	cran = "tab" 

	version("5.1.1", md5="c89a124985eb85c3a0c95cfe4b3571ec")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survey@4.1:", type=("build", "run"))
