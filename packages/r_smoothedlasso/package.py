# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothedlasso(RPackage):
	"""A Framework to Smooth L1 Penalized Regression Operators using
Nesterov Smoothing

	We provide full functionality to smooth L1 penalized regression operators and to compute regression estimates thereof. For this, the objective function of a user-specified regression operator is first smoothed using Nesterov smoothing (see Y. Nesterov (2005) <doi:10.1007/s10107-004-0552-5>), resulting in a modified objective function with explicit gradients everywhere. The smoothed objective function and its gradient are minimized via BFGS, and the obtained minimizer is returned. Using Nesterov smoothing, the smoothed objective function can be made arbitrarily close to the original (unsmoothed) one. In particular, the Nesterov approach has the advantage that it comes with explicit accuracy bounds, both on the L1/L2 difference of the unsmoothed to the smoothed objective functions as well as on their respective minimizers (see G. Hahn, S.M. Lutz, N. Laha, C. Lange (2020) <doi:10.1101/2020.09.17.301788>). A progressive smoothing approach is provided which iteratively smoothes the objective function, resulting in more stable regression estimates. A function to perform cross validation for selection of the regularization parameter is provided.
	"""
	
	cran = "smoothedLasso" 

	version("1.6", md5="f532f0e4e7d8369e9c1b98d1a11dc7ab")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
