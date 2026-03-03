# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNjtr1(RPackage):
	"""Download, Analyze & Clean New Jersey Car Crash Data

	Download and analyze motor vehicle crash data released by the New Jersey Department of Transportation (NJDOT).
  The data in this package is collected through the filing of NJTR-1 form by police officers, which provide a standardized way of documenting a motor vehicle crash that occurred in New Jersey.
  3 different data tables containing data on crashes, vehicles & pedestrians released from 2001 to the present can be downloaded & cleaned using this package.
	"""
	
	homepage = "https://gavinrozzi.github.io/njtr1/"
	cran = "njtr1" 

	version("0.3.2", md5="705d3bbc228cfdb70a885d835e806db1", url="https://cran.r-project.org/src/contrib/njtr1_0.3.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
