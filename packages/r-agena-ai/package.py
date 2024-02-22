# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgenaAi(RPackage):
	"""R Wrapper for 'agena.ai' API

	An R wrapper for 'agena.ai' <https://www.agena.ai> which provides users capabilities to work with 'agena.ai' using the R environment. Users can create Bayesian network models from scratch or import existing models in R and export to 'agena.ai' cloud or local API for calculations. Note: running calculations requires a valid 'agena.ai' API license (past the initial trial period of the local API).
	"""
	
	cran = "agena.ai" 

	version("1.1.1", md5="a2103c038533e983a45925411d6ab546")

	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
