# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgmanalysis(RPackage):
	"""Clean and Analyze Continuous Glucose Monitor Data

	This code provides several different functions for cleaning and analyzing continuous glucose monitor data. Currently it works with 'Dexcom', 'iPro 2', 'Diasend', 'Libre', or 'Carelink' data. The cleandata() function takes a directory of CGM data files and prepares them for analysis. cgmvariables() iterates through a directory of cleaned CGM data files and produces a single spreadsheet with data for each file in either rows or columns. The column format of this spreadsheet is compatible with REDCap data upload. cgmreport() also iterates through a directory of cleaned data, and produces PDFs of individual and aggregate AGP plots. Please visit <https://github.com/childhealthbiostatscore/R-Packages/> to download the new-user guide.
	"""
	
	cran = "cgmanalysis" 

	version("2.7.7", md5="2b55d19b722811039dfccadd2d1a1b9e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
