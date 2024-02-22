# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScorecard(RPackage):
	"""Credit Risk Scorecard

	
  The `scorecard` package makes the development of credit risk scorecard 
  easier and efficient by providing functions for some common tasks, 
  such as data partition, variable selection, woe binning, scorecard scaling,
  performance evaluation and report generation. These functions can also used
  in the development of machine learning models.
    The references including: 
  1. Refaat, M. (2011, ISBN: 9781447511199). Credit Risk Scorecard: 
  Development and Implementation Using SAS. 
  2. Siddiqi, N. (2006, ISBN: 9780471754510). Credit risk scorecards. 
  Developing and Implementing Intelligent Credit Scoring.
	"""
	
	homepage = "https://github.com/ShichenXie/scorecard"
	cran = "scorecard" 

	version("0.4.3", md5="0305e355e16b0719a58b50e9118b7cfe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xefun@0.1.3:", type=("build", "run"))
