# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKofdata(RPackage):
	"""Get Data from the 'KOF Datenservice' API

	Read Swiss time series data from the 'KOF Data' API, <https://datenservice.kof.ethz.ch>. The API provides macro economic time series data mostly about Switzerland. The package itself is a set of wrappers around the 'KOF Datenservice' API. The 'kofdata' package is able to consume public information as well as data that requires an API token. 
	"""
	
	homepage = "https://github.com/KOF-ch/kofdata"
	cran = "kofdata" 

	version("0.2.1", md5="d3d35a5bec10d614a5f088d5610782af")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
