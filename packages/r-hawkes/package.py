# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHawkes(RPackage):
	"""Hawkes process simulation and calibration toolkit

	The package allows to simulate Hawkes process both in univariate and multivariate settings. It gives functions to compute different moments of the number of jumps of the process on a given interval, such as mean, variance or autocorrelation of process jumps on time intervals separated by a lag.
	"""
	
	cran = "hawkes" 

	version("0.0-4", md5="1b379f60e2ecf88ae5efd0cde251c130")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.100.2.1:", type=("build", "run"))
