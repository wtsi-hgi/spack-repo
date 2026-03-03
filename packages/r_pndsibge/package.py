# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPndsibge(RPackage):
	"""Downloading, Reading and Analyzing PNDS Microdata - Package in
Development

	Provides tools for downloading, reading and analyzing the National
  Survey of Demographic and Health - PNDS, a household survey from Brazilian Institute
  of Geography and Statistics - IBGE. The data must be downloaded from the official
  website <https://www.ibge.gov.br/>. Further analysis must be made using package 'survey'.
	"""
	
	cran = "PNDSIBGE" 

	version("0.1.1", md5="7e51f6f2f835d0e79dc8492fc7ffcfd1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-projmgr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
