# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaleobiodb(RPackage):
	"""Download and Process Data from the Paleobiology Database

	Includes functions to wrap most endpoints of the 'PaleobioDB'
    API and functions to visualize and process the fossil data. The API
    documentation for the Paleobiology Database can be found at
    <https://paleobiodb.org/data1.2/>.
	"""
	
	homepage = "https://docs.ropensci.org/paleobioDB/"
	cran = "paleobioDB" 

	version("1.0.0", md5="120ac86676303efaf78e5c2627e47f61")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
