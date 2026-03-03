# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyhedralcubature(RPackage):
	"""Multiple Integration over Convex Polyhedra

	Evaluation of multiple integrals over convex polyhedra. This
    is useful when the bounds of the integrals are some linear
    combinations of the variables.
	"""
	
	homepage = "https://github.com/stla/polyhedralCubature"
	cran = "polyhedralCubature" 

	version("1.1.0", md5="973200896c58fba2d491d755acd0e0c8")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ompr", type=("build", "run"))
	depends_on("r-qspray", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-simplicialcubature", type=("build", "run"))
	depends_on("r-spray", type=("build", "run"))
	depends_on("r-tessellation", type=("build", "run"))
