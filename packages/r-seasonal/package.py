# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeasonal(RPackage):
	"""R Interface to X-13-ARIMA-SEATS

	Easy-to-use interface to X-13-ARIMA-SEATS, the seasonal adjustment
    software by the US Census Bureau. It offers full access to almost all
    options and outputs of X-13, including X-11 and SEATS, automatic ARIMA model
    search, outlier detection and support for user defined holiday variables,
    such as Chinese New Year or Indian Diwali. A graphical user interface can be
    used through the 'seasonalview' package. Uses the X-13-binaries from the
    'x13binary' package.
	"""
	
	homepage = "http://www.seasonal.website"
	cran = "seasonal" 

	version("1.9.0", md5="366472ed834aa2a4f4d6a05bf7e493ca")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-x13binary", type=("build", "run"))
