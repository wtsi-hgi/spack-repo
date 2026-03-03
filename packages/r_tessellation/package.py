# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTessellation(RPackage):
	"""Delaunay and Voronoï Tessellations

	Delaunay and Voronoï tessellations, with emphasis on the
    two-dimensional and the three-dimensional cases (the package provides
    functions to plot the tessellations for these cases). Delaunay
    tessellations are computed in C with the help of the 'Qhull' library
    <http://www.qhull.org/>.
	"""
	
	homepage = "https://github.com/stla/tessellation"
	cran = "tessellation" 

	version("2.3.0", md5="6ea3107c399f3acf707d41642afa752a")

	depends_on("r-colorsgen", type=("build", "run"))
	depends_on("r-cxhull", type=("build", "run"))
	depends_on("r-english", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rvcg", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
