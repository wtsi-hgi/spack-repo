# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExceldata(RPackage):
	"""Streamline Data Import, Cleaning and Recoding from 'Excel'

	A small group of functions to read in a data dictionary and the
    corresponding data table from 'Excel' and to automate the cleaning, re-coding
    and creation of simple calculated variables. This package was designed to
    be a companion to the macro-enabled 'Excel' template available
    on the GitHub site, but works with any similarly-formatted 'Excel' data.
	"""
	
	cran = "exceldata" 

	version("0.1.1.3", md5="0903d0a5e13fa91786dd1fc7a32d77d7")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
