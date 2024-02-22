# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGensphere(RPackage):
	"""Generalized Spherical Distributions

	Define and compute with generalized spherical distributions - multivariate probability
 laws that are specified by a star shaped contour (directional behavior) and a radial component.
 The methods are described in Nolan (2016) <doi:10.1186/s40488-016-0053-0>.
	"""
	
	cran = "gensphere" 

	version("1.3", md5="aa2c9fac0ee2bb11ad6df55add3817cf")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvmesh", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-sphericalcubature@1.5:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-simplicialcubature", type=("build", "run"))
