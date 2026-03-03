# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanic(RPackage):
	"""Location Identify Tool

	Determine the sea area where the fishing boat operates. 
             The latitude and longitude of geographic coordinates are used to match oceanic areas and economic sea areas. 
	    	     You can plot the distribution map with dotplot() function.
		         Please refer to Flanders Marine Institute (2020) <doi:10.14284/403>.
	"""
	
	cran = "oceanic" 

	version("0.1.6", md5="12e6cbedd69e56178e8a9ca79442006b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
