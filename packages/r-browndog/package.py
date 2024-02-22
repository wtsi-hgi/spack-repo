# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrowndog(RPackage):
	"""Brown Dog R Interface

	An R interface for the Brown Dog which allows researchers to leverage Brown Dog Services 
    that provides modules to identify the conversion options for a file, to convert file to appropriate
    format, or to extract data from a file. See <http://browndog.ncsa.illinois.edu/> for more information.  
	"""
	
	cran = "BrownDog" 

	version("0.2.1", md5="cffa71b3ba2439969f87343996c6c6a7")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
