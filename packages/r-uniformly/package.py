# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniformly(RPackage):
	"""Uniform Sampling

	Uniform sampling on various geometric shapes, such as
    spheres, ellipsoids, simplices.
	"""
	
	homepage = "https://github.com/stla/uniformly"
	cran = "uniformly" 

	version("0.5.0", md5="72666575778e44deb070e4fb6170462c")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-pgnorm", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
