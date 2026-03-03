# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwfy(RPackage):
	"""Drive the API for TheyWorkForYou

	An R wrapper around the API of TheyWorkForYou, a parliamentary 
    monitoring site that scrapes and repackages Hansard (the UK's parliamentary 
    record) and augments it with information from the Register of Members' 
    Interests, election results, and voting records to provide a unified 
    source of information about UK legislators and their activities. See 
    <http://www.theyworkforyou.com> for details.
	"""
	
	homepage = "https://conjugateprior.github.io/twfy"
	cran = "twfy" 

	version("0.1.0", md5="dbcc377848bac7753a7ab0d631ff49bd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
