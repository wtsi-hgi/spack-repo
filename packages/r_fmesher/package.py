# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmesher(RPackage):
	"""Triangle Meshes and Related Geometry Tools

	Generate planar and spherical triangle meshes,
    compute finite element calculations for 1- and 2-dimensional flat and curved
    manifolds with associated basis function spaces, methods for lines and
    polygons, and transparent handling of coordinate reference systems and
    coordinate transformation, including 'sf' and 'sp' geometries. The core
    'fmesher' library code was originally part of the 'INLA' package, and
    implements parts of "Triangulations and Applications" by
    Hjelle and Daehlen (2006) <doi:10.1007/3-540-33261-8>.
	"""
	
	homepage = "https://inlabru-org.github.io/fmesher/"
	cran = "fmesher" 

	version("0.1.5", md5="f6b3da0784dc165b92645e811310fe54")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp@1.6.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
