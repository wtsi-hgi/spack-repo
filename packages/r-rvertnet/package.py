# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvertnet(RPackage):
	"""Search 'Vertnet', a 'Database' of Vertebrate Specimen Records

	Retrieve, map and summarize data from the 'VertNet.org' 
    archives (<https://vertnet.org/>).  Functions allow searching by many 
    parameters, including 'taxonomic' names, places, and dates. In addition, 
    there is an interface for conducting spatially delimited searches, and 
    another for requesting large 'datasets' via email.
	"""
	
	homepage = "https://github.com/ropensci/rvertnet"
	cran = "rvertnet" 

	version("0.8.4", md5="9d99ab388ded03a97d32bd95e5508742")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-crul@0.5.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
