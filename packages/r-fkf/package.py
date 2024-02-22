# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFkf(RPackage):
	"""Fast Kalman Filter

	This is a fast and flexible implementation of the Kalman
        filter and smoother, which can deal with NAs. It is entirely written in C and relies fully on linear algebra subroutines contained in
        BLAS and LAPACK. Due to the speed of the filter, the fitting of
        high-dimensional linear state space models to large datasets
        becomes possible. This package also contains a plot function
        for the visualization of the state vector and graphical
        diagnostics of the residuals.
	"""
	
	homepage = "https://waternumbers.github.io/FKF/"
	cran = "FKF" 

	version("0.2.5", md5="7ec01dbd40d252f3497c180dd8877e8a")

	depends_on("r@3.5:", type=("build", "run"))
