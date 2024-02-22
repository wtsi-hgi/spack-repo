# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMondate(RPackage):
	"""Keep Track of Dates in Terms of Months

	Keep track of dates in terms of fractional calendar months 
  per Damien Laker "Time Calculations for Annualizing Returns: the Need for Standardization", 
  The Journal of Performance Measurement, 2008.
  Model dates as of close of business.
  Perform date arithmetic in units of "months" and "years".
  Allow "infinite" dates to model "ultimate" time.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "mondate" 

	version("1.0", md5="f539309d174641a8caa2730c5d451e48")

	depends_on("r@3:", type=("build", "run"))
