# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnrs(RPackage):
	"""Access the 'Geographic Name Resolution Service'

	Provides tools for interacting with the 'geographic name resolution service' ('GNRS') API <https://github.com/ojalaquellueva/gnrs> and associated functionality. The 'GNRS' is a batch application for resolving & standardizing political division names against standard name in the geonames database <http://www.geonames.org/>. The 'GNRS' resolves political division names at three levels: country, state/province and county/parish. Resolution is performed in a series of steps, beginning with direct matching to standard names, followed by direct matching to alternate names in different languages, followed by direct matching to standard codes (such as ISO and FIPS codes). If direct matching fails, the 'GNRS' attempts to match to standard and then alternate names using fuzzy matching, but does not perform fuzzing matching of political division codes. The 'GNRS' works down the political division hierarchy, stopping at the current level if all matches fail. In other words, if a country cannot be matched, the 'GNRS' does not attempt to match state or county.
	"""
	
	cran = "GNRS" 

	version("0.3.4", md5="d0237a61d4dd65dcadd785efc70a7a5f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
