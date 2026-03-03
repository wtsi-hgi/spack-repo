# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkenyaforex(RPackage):
	"""Historical Data for Kenya Foreign Exchange Prices

	Exchange rate for Kenya Shilling against other currencies, US DOLLAR, EURO, STERLING POUND, Tanzania Shilling, Uganda Shilling.
	"""
	
	cran = "rKenyaForex" 

	version("0.1.0", md5="f6acb77df47c32041c98633ad9dff16b")

	depends_on("r@2.10:", type=("build", "run"))
