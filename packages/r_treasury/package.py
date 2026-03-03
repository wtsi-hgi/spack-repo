# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreasury(RPackage):
	"""US Treasury XML Feed Wrapper

	Download daily interest rates from the US Treasury XML feed.
    Leveraging
    <https://home.treasury.gov/treasury-daily-interest-rate-xml-feed>,
    this package serves as a wrapper, facilitating the retrieval of daily
    treasury rates across various categories, including par yield curves,
    treasury bills, long-term rates, and real yield curves.
	"""
	
	homepage = "https://m-muecke.github.io/treasury/"
	cran = "treasury" 

	version("0.1.0", md5="7affb582d175939cd4c30041cc32d792")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
