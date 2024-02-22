# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantdates(RPackage):
	"""Manipulate Dates for Finance

	Functions to manipulate dates and count days for quantitative finance analysis. The 'quantdates' package considers leap, holidays and business days for relevant calendars in a financial context to simplify quantitative finance calculations, consistent with International Swaps and Derivatives Association (ISDA) (2006) <https://www.isda.org/book/2006-isda-definitions/> regulations.
	"""
	
	cran = "quantdates" 

	version("1.0", md5="c522122cac8311f2b292fd65a9f7a2db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
