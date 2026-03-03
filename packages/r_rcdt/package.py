# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcdt(RPackage):
	"""Fast 2D Constrained Delaunay Triangulation

	Performs 2D Delaunay triangulation, constrained or
    unconstrained, with the help of the C++ library 'CDT'. A function to
    plot the triangulation is provided. The constrained Delaunay
    triangulation has applications in geographic information systems.
	"""
	
	homepage = "https://github.com/stla/RCDT"
	cran = "RCDT" 

	version("1.3.0", md5="b355e6e788d87442500d5282b30d981b")

	depends_on("r-colorsgen", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
