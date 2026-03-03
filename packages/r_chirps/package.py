# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChirps(RPackage):
	"""API Client for CHIRPS and CHIRTS

	API Client for the Climate Hazards Center 'CHIRPS' and 'CHIRTS'. 
  The 'CHIRPS' data is a quasi-global (50°S – 50°N) high-resolution 
  (0.05 arc-degrees) rainfall data set, which incorporates satellite imagery 
  and in-situ station data to create gridded rainfall time series for trend 
  analysis and seasonal drought monitoring. 'CHIRTS' is a quasi-global 
  (60°S – 70°N), high-resolution data set of daily maximum and minimum
  temperatures. For more details on 'CHIRPS' and 'CHIRTS' data please visit 
  its official home page <https://www.chc.ucsb.edu/data>.
	"""
	
	homepage = "https://docs.ropensci.org/chirps/"
	cran = "chirps" 

	version("0.1.4", md5="77cbae2b1378bcf960aee2fdd2c58e3c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra@1.2.10:", type=("build", "run"))
