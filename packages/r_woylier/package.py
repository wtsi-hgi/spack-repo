# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoylier(RPackage):
	"""Alternative Tour Frame Interpolation Method

	This method generates a tour path by interpolating between d-D frames in p-D using Givens rotations. The algorithm arises from the problem of zeroing elements of a matrix. This interpolation method is useful for showing specific d-D frames in the tour, as opposed to d-D planes, as done by the geodesic interpolation. It is useful for projection pursuit indexes which are not s invariant. See Buja et al (2005) <doi:10.1016/S0169-7161(04)24014-7>. 
	"""
	
	cran = "woylier" 

	version("0.0.5", md5="27537d4206425935395f110116ef7a45")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tourr", type=("build", "run"))
	depends_on("r-geozoo", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
