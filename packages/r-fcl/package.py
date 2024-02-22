# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcl(RPackage):
	"""A Financial Calculator

	A financial calculator that provides very fast implementations
    of common financial indicators using 'Rust' code. It includes functions for
    bond-related indicators, such as yield to maturity ('YTM'), modified duration,
    and Macaulay duration, as well as functions for calculating time-weighted
    and money-weighted rates of return (using 'Modified Dietz' method) for multiple portfolios,
    given their market values and profit and loss ('PnL') data. 'fcl' is designed
    to be efficient and accurate for financial analysis and computation. The methods
    used in this package are based on the following references:
    <https://en.wikipedia.org/wiki/Modified_Dietz_method>,
    <https://en.wikipedia.org/wiki/Time-weighted_return>.
	"""
	
	homepage = "https://github.com/shrektan/fcl"
	cran = "fcl" 

	version("0.1.0", md5="8e6f24a3e745f2564cda7a7eec70eb0b")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-ymd", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
