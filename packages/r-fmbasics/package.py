# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmbasics(RPackage):
	"""Financial Market Building Blocks

	Implements basic financial market objects like currencies, currency
  pairs, interest rates and interest rate indices. You will be able to use
  Benchmark instances of these objects which have been defined using their most
  common conventions or those defined by International Swap Dealer Association
  (ISDA, <https://www.isda.org>) legal documentation. 
	"""
	
	homepage = "https://github.com/imanuelcostigan/fmbasics"
	cran = "fmbasics" 

	version("0.3.0", md5="553cf55d3f40fe1522daa46202dc8f66")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-fmdates@0.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
