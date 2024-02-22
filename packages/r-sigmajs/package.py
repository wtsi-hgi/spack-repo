# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigmajs(RPackage):
	"""Interface to 'Sigma.js' Graph Visualization Library

	Interface to 'sigma.js' graph visualization library including animations, plugins and shiny proxies.
	"""
	
	homepage = "http://sigmajs.john-coene.com/"
	cran = "sigmajs" 

	version("0.1.5", md5="bbc50eff21195d534ad89503ca816511")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
