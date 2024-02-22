# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZ10(RPackage):
	"""Simple Ecological Statistics from the NEON Network

	Provides simple statistics from instruments and observations at sites in the NEON network, and acts as a simple interface for v0 of the National Ecological Observatory Network (NEON) API.
  Statistics are generated for meteorologic and soil-based observations, and are presented for daily, annual, and one-time observations at all available NEON sites.
  Users can also retrieve any dataset publicly hosted by NEON. Metadata for NEON sites and data products can be returned, as well as information on data product availability by site and date. 
  For more information on NEON, please visit <https://www.neonscience.org>. For detailed data product information, please see the NEON data product catalog at <https://data.neonscience.org/data-product-catalog>.
	"""
	
	cran = "Z10" 

	version("0.1.0", md5="fbdc096c0ff4241e80f51ace38df6f16", url="https://cran.r-project.org/src/contrib/Z10_0.1.0.tar.gz")

	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
