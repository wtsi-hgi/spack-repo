# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2country(RPackage):
	"""Country Data with Names, Capitals, Currencies, Populations,
Time, Languages and so on

	Obtain information about countries around the globe. Information for names, states, languages, time, capitals, currency and many more. Data source are 'Wikipedia' <https://www.wikipedia.org>, 'TimeAndDate' <https://www.timeanddate.com> and 'CountryCode' <https://countrycode.org>.
	"""
	
	homepage = "https://r2country.obi.obianom.com"
	cran = "r2country" 

	version("2.0.2.3.1", md5="402d58a03dcb20088303d8a42c2708ff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-quickcode", type=("build", "run"))
