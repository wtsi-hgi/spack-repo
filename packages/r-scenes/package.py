# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScenes(RPackage):
	"""Switch Between Alternative 'shiny' UIs

	Sometimes it is useful to serve up alternative 'shiny' UIs 
    depending on information passed in the request object, such as the value of 
    a cookie or a query parameter. This packages facilitates such switches.
	"""
	
	homepage = "https://github.com/r4ds/scenes"
	cran = "scenes" 

	version("0.1.0", md5="03cb174143dee7b906a0b67874bec998")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cookies", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
