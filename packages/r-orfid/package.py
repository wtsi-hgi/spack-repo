# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrfid(RPackage):
	"""Manage and Summarize Data from Oregon RFID ORMR and ORSR Antenna
Readers

	Automates and standardizes the import of raw data from Oregon RFID (radio-frequency identification) ORMR (Oregon RFID Multi-Reader) and ORSR (Oregon RFID Single Reader) antenna readers. Compiled data can then be combined within multi-reader arrays for further analysis, including summarizing tag and reader detections, determining tag direction, and calculating antenna efficiency.
	"""
	
	homepage = "https://github.com/hugo-marques/ORFID"
	cran = "ORFID" 

	version("1.0.2", md5="b10c6bc39c965b000bf3af17aa3009e3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
