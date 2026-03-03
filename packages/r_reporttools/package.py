# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReporttools(RPackage):
	"""Generate "LaTeX"" Tables of Descriptive Statistics

	These functions are especially helpful when writing reports of data analysis using "Sweave".
	"""
	
	homepage = "http://www.kasparrufibach.ch"
	cran = "reporttools" 

	version("1.1.3", md5="1ddb20faab251c8fc504bda5f60c4259")

	depends_on("r-xtable", type=("build", "run"))
