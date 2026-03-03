# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerbir(RPackage):
	"""An Interface to the 'Power BI REST APIs'

	Makes it easy to push data to 'Power BI' using R and the 'Power BI 
    REST APIs' (see <https://docs.microsoft.com/en-us/rest/api/power-bi/>). 
    A set of functions for turning data frames into 'Power BI' datasets and 
    refreshing these datasets are provided. Administrative tasks such as 
    monitoring refresh statuses and pulling metadata about workspaces and users
    are also supported.
	"""
	
	cran = "powerbiR" 

	version("0.1.0", md5="0902a930fb6c0f12cd407f7f8fa206a1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-azureauth", type=("build", "run"))
