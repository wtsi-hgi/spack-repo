# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPropubbills(RPackage):
	"""'ProPublica' U.S. Congress Bills API Wrapper

	An API wrapper around the 'ProPublica' API <https://projects.propublica.org/api-docs/congress-api/> for U.S. Congressional Bills. Users can include their API key, U.S. Congress, branch, and offset ranges, to return a dataframe of all results within those parameters. This package is different from the 'RPublica' package because it is for the 'ProPublica' U.S. Congress data API, and the 'RPublica' package is for the Nonprofit Explorer, Forensics, and Free the Files data APIs. 
	"""
	
	cran = "proPubBills" 

	version("0.1", md5="16f9af4c42292bd75c55bd54838b40fe")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
