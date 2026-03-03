# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeofkf(RPackage):
	"""Kriging Method for Spatial Functional Data

	A Kriging method for functional datasets with spatial dependency.
    This functional Kriging method avoids the need to estimate the
    trace-variogram, and the curve is estimated by minimizing a quadratic
    form. The curves in the functional dataset are smoothed using Fourier
    series. The functional Kriging of this package is a modification of the
    method proposed by Giraldo (2011) <doi:10.1007/s10651-010-0143-y>.
	"""
	
	homepage = "https://github.com/gilberto-sassi/geoFKF"
	cran = "geoFKF" 

	version("0.1.1", md5="7aff37fc8fa5a2bc829a16b548638ce4")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
