# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadwords(RPackage):
	"""Loading Google Adwords Data into R

	Aims at loading Google Adwords data into R. Adwords is an online
    advertising service that enables advertisers to display advertising copy to web
    users (see <https://developers.google.com/adwords/> for more information). 
    Therefore the package implements three main features. First, the package
    provides an authentication process for R with the Google Adwords API (see 
    <https://developers.google.com/adwords/api/> for more information) via OAUTH2.
    Second, the package offers an interface to apply the Adwords query language in
    R and query the Adwords API with ad-hoc reports. Third, the received data are
    transformed into suitable data formats for further data processing and data
    analysis.
	"""
	
	homepage = "https://github.com/jburkhardt/RAdwords"
	cran = "RAdwords" 

	version("0.1.18", md5="76e0d6621b1ac0e2c0f234ef23dcb0f7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
