# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBslib(RPackage):
	"""Custom 'Bootstrap' 'Sass' Themes for 'shiny' and 'rmarkdown'.

	Simplifies custom 'CSS' styling of both 'shiny' and 'rmarkdown' via
	'Bootstrap' 'Sass'. Supports both 'Bootstrap' 3 and 4 as well as their
	various 'Bootswatch' themes. An interactive widget is also provided for
	previewing themes in real time."""

	cran = "bslib"

	license("MIT")

	version("0.6.1", md5="688035c1317d99324ef73bb5100664b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-htmltools@0.5.7:", type=("build", "run"))
	depends_on("r-jquerylib@0.1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-memoise@2.0.1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sass@0.4:", type=("build", "run"))
