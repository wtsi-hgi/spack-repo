# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactableExtras(RPackage):
	"""Extra Features for 'reactable' Package

	Enhanced functionality for 'reactable' in 'shiny' applications, offering interactive and dynamic data table capabilities with ease.
    With 'reactable.extras', easily integrate a range of functions and components to enrich your 'shiny' apps and facilitate user-friendly data exploration.
	"""
	
	homepage = "https://appsilon.github.io/reactable.extras/"
	cran = "reactable.extras" 

	version("0.2.0", md5="b8af3b378e8726b0ec1853a9f6e62a10")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-reactable@0.4:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
