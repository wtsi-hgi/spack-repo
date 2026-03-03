# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcelr(RPackage):
	"""A Wrapper of the 'JavaScript' Library 'jExcel'

	An R interface to 'jExcel' library to create web-based interactive tables and spreadsheets compatible with 'Excel' or any other spreadsheet software.
	"""
	
	homepage = "https://github.com/Swechhya/excelR"
	cran = "excelR" 

	version("0.4.0", md5="9c48a33224aee3f039de27225d3b9469")

	depends_on("r-htmlwidgets@1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
