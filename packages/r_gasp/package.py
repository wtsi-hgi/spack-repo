# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGasp(RPackage):
	"""Train and Apply a Gaussian Stochastic Process Model

	Train a Gaussian stochastic process model of an unknown function, possibly observed with error, via maximum likelihood or maximum a posteriori (MAP) estimation, run model diagnostics, and make predictions, following Sacks, J., Welch, W.J., Mitchell, T.J., and Wynn, H.P. (1989) "Design and Analysis of Computer Experiments", Statistical Science, <doi:10.1214/ss/1177012413>.  Perform sensitivity analysis and visualize low-order effects, following Schonlau, M. and Welch, W.J. (2006), "Screening the Input Variables to a Computer Model Via Analysis of Variance and Visualization", <doi:10.1007/0-387-28014-6_14>.
	"""
	
	cran = "GaSP" 

	version("1.0.5", md5="86da73d5a24e941fd419d85e513e165a")

	depends_on("r@3.5:", type=("build", "run"))
