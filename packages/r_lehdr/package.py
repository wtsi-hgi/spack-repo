# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLehdr(RPackage):
	"""Grab Longitudinal Employer-Household Dynamics (LEHD) Flat Files

	Designed to query Longitudinal Employer-Household Dynamics (LEHD) 
    workplace/residential association and origin-destination flat files and 
    optionally aggregate Census block-level data to block group, tract, county, 
    or state. Data comes from the LODES FTP server <https://lehd.ces.census.gov/data/lodes/LODES8/>.
	"""
	
	homepage = "https://github.com/jamgreen/lehdr/"
	cran = "lehdr" 

	version("1.1.3", md5="4d9ec5446c964514782fc403b55dbdf4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
