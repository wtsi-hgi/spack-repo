# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallelplot(RPackage):
	"""'Htmlwidget' for a Parallel Coordinates Plot

	Create a parallel coordinates plot, using 'htmlwidgets' package and 'd3.js'.
	"""
	
	homepage = "https://gitlab.com/drti/parallelplot"
	cran = "parallelPlot" 

	version("0.3.1", md5="14db25c1e1b0a608f5a2e78d51a33e24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
