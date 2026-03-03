# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REodhd(RPackage):
	"""Official 'eodhd' API R Financial Library

	Official 'eodhd' API R Library. It helps to get and work with financial data,
              historical data and etc. API reference available at <https://eodhd.com/financial-apis/>.
	"""
	
	homepage = "https://github.com/EodHistoricalData/EODHD-APIs-R-Financial-Library"
	cran = "eodhd" 

	version("1.0.4", md5="0aac687b2083c16c6749481291cef4ed")

	depends_on("r-httr", type=("build", "run"))
