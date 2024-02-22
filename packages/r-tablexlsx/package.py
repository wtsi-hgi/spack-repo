# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablexlsx(RPackage):
	"""Export Data Frames to Excel Workbook

	Collection of functions that allow to export data frames to excel workbook.
	"""
	
	homepage = "https://ddotta.github.io/tablexlsx/"
	cran = "tablexlsx" 

	version("0.1.0", md5="98a0847d6ab24f8e619b940fec083f01")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
