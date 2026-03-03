# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeda(RPackage):
	"""'Hydropeaking Events Detection Algorithm'

	This tool identifies hydropeaking events from raw time-series flow record, a rapid flow variation induced by the hourly-adjusted electricity market. The novelty of 'HEDA' is to use vector angle instead of the first-order derivative to detect change points which not only largely improves the computing efficiency but also accounts for the rate of change of the flow variation. More details <doi:10.1016/j.jhydrol.2021.126392>.
	"""
	
	cran = "HEDA" 

	version("0.1.5", md5="d71aa996ceec698a1963980fa0aa48ff")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-zoo@1.8.7:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
