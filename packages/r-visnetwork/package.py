# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisnetwork(RPackage):
	"""Network Visualization using 'vis.js'

	An R package for network visualization using 'vis.js' library. Provides an
	interface to create interactive network graphs.
	"""

	cran = "visNetwork"

	version("2.1.2", sha256="47c99d42fc89e6ae929257b2648d998c5ffed60dff97ad7e47613f5a0c1ddc84")
	version("2.1.0", sha256="f6f0cc0f0f131a32159ff8fefccea4b4ea9b45af21fd431a8d75dcc712f5168a")

	depends_on("r@3.0:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
