# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsomemo(RPackage):
	"""Retrieve Data using the 'IsoMemo' API

	API wrapper that contains functions to retrieve data from the 'IsoMemo' partnership databases. Web services for API: <https://isomemodb.com/api/v1/iso-data>. 
	"""
	
	cran = "IsoMemo" 

	version("23.10.1", md5="a0d42f52f2fc678fb75644af3fd7424a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-modules", type=("build", "run"))
