# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTourr(RPackage):
	"""Tour Methods for Multivariate Data Visualisation

	Implements geodesic interpolation and basis
    generation functions that allow you to create new tour
    methods from R.
	"""
	
	homepage = "https://github.com/ggobi/tourr"
	cran = "tourr" 

	version("1.1.0", md5="b12dd810368266e4272f3a50e199f1fc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
