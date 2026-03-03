# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyauthr(RPackage):
	"""'Shiny' Authentication Modules

	Add in-app user authentication to 'shiny', 
    allowing you to secure publicly hosted apps and 
    build dynamic user interfaces from user information.
	"""
	
	homepage = "https://github.com/paulc91/shinyauthr"
	cran = "shinyauthr" 

	version("1.0.0", md5="bfa5e9d117e30e23a5bd25206890d73e")

	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
