# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaersquarterlydata(RPackage):
	"""FDA Adverse Event Reporting System Quarterly Data Extracting
Tool

	An easy framework to read FDA Adverse Event Reporting System XML/ASCII files <https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-latest-quarterly-data-files>.
	"""
	
	cran = "faersquarterlydata" 

	version("1.1.0", md5="2b7fecb84387d19124cfccb1d3f3db1c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
