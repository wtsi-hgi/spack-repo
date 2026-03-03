# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterpolation(RPackage):
	"""Interpolation of Bivariate Functions

	Provides two different methods, linear and nonlinear, to
    interpolate a bivariate function, scalar-valued or vector-valued. 
    The interpolated data are not necessarily gridded. The algorithms 
    are performed by the 'C++' library 'CGAL' (<https://www.cgal.org/>).
	"""
	
	homepage = "https://github.com/stla/interpolation"
	cran = "interpolation" 

	version("0.1.1", md5="a8e6f61d4cf274fb6dc04faa0c49d88e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
