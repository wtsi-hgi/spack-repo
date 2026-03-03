# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloudos(RPackage):
	"""R Client Library for CloudOS

	The 'CloudOS' client library for R makes it easy to interact with 
    CloudOS in the R environment for analysis.
	"""
	
	homepage = "https://github.com/lifebit-ai/cloudos"
	cran = "cloudos" 

	version("0.4.0", md5="49dc9a1f7e1192e92e8cd969be705d6e")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
