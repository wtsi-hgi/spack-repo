# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RData360r(RPackage):
	"""Wrapper for 'TCdata360' and 'Govdata360' API

	Makes it easy to engage with the Application Program Interface (API)
    of the 'TCdata360' and 'Govdata360' platforms at <https://tcdata360.worldbank.org/>
    and <https://govdata360.worldbank.org/>, respectively.
    These application program interfaces provide access to over 5000 trade, competitiveness, and governance
    indicator data, metadata, and related information from sources
    both inside and outside the World Bank Group.
    Package functions include easier download of data sets, metadata, and
    related information, as well as searching based on user-inputted query.
	"""
	
	homepage = "https://github.com/mrpsonglao/data360r"
	cran = "data360r" 

	version("1.0.9", md5="24e52e3b16ceab38ee908c4ffe57d77b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
