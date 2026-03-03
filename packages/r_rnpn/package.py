# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnpn(RPackage):
	"""Interface to the National 'Phenology' Network 'API'

	Programmatic interface to the
    Web Service methods provided by the National 'Phenology' Network
    (<https://usanpn.org/>), which includes data on various life history
    events that occur at specific times.
	"""
	
	homepage = "https://github.com/usa-npn/rnpn"
	cran = "rnpn" 

	version("1.2.8.0", md5="f3e52449179e030cb7a60f660ec6952c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-sp@1.1.0:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
