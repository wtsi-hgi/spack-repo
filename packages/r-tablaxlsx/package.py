# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablaxlsx(RPackage):
	"""Write Formatted Tables in Excel Workbooks

	For writing tables with custom formats in a Excel file ready to be distributed.
	"""
	
	cran = "tablaxlsx" 

	version("1.2.5", md5="3512b52b3bb512dead73adc60f01fa63")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
