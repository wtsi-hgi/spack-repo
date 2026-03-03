# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNso1212(RPackage):
	"""National Statistical Office of Mongolia's Open Data API Handler

	National Statistical Office of Mongolia (NSO) is the national statistical service and an organization of Mongolian government. NSO provides open access to official data via its API <http://opendata.1212.mn/en/doc>. The package NSO1212 has functions for accessing the API service. The functions are compatible with the API v2.0 and get data sets and its detailed informations from the API.
	"""
	
	homepage = "https://github.com/galaamn/NSO1212"
	cran = "NSO1212" 

	version("1.4.0", md5="8a851d9d1f3d72232f3f9433e171cec8", url="https://cran.r-project.org/src/contrib/NSO1212_1.4.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
