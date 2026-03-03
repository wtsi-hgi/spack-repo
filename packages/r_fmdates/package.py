# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmdates(RPackage):
	"""Financial Market Date Calculations

	Implements common date calculations relevant for specifying
  the economic nature of financial market contracts that are typically defined
  by International Swap Dealer Association (ISDA, <http://www2.isda.org>) legal
  documentation. This includes methods to check whether dates are business
  days in certain locales, functions to adjust and shift dates and time length
  (or day counter) calculations.
	"""
	
	homepage = "https://github.com/imanuelcostigan/fmdates"
	cran = "fmdates" 

	version("0.1.4", md5="8b2b7dc96985d828ca69f8291b9c6f0b")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
