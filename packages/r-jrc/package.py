# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJrc(RPackage):
	"""Exchange Commands Between R and 'JavaScript'

	An 'httpuv' based bridge between R and 'JavaScript'. Provides an easy way to exchange commands and data between a web page and a currently running R session. 
	"""
	
	homepage = "https://github.com/anders-biostat/jrc"
	cran = "jrc" 

	version("0.6.0", md5="6de36a9a56f01c28a47dbf1987f0aa19")

	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
