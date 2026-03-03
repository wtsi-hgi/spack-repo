# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCansim2r(RPackage):
	"""Directly Extracts Complete CANSIM Data Tables

	Extract CANSIM (Statistics Canada) tables and transform them into readily usable data in panel (wide) format. It can also extract more than one table at a time and produce the resulting merge by time period and geographical region.
	"""
	
	cran = "CANSIM2R" 

	version("1.14.1", md5="602e7ac18fa445092b8cd14d1e75f670")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
