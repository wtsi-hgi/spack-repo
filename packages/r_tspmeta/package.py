# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTspmeta(RPackage):
	"""Instance Feature Calculation and Evolutionary Instance
Generation for the Traveling Salesman Problem

	Instance feature calculation and evolutionary instance generation
    for the traveling salesman problem. Also contains code to "morph" two TSP
    instances into each other. And the possibility to conveniently run a couple
    of solvers on TSP instances.
	"""
	
	homepage = "https://github.com/berndbischl/tspmeta"
	cran = "tspmeta" 

	version("1.2", md5="7b002b1be008e3caa3c1e3e851c80c05")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate@1.5:", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
