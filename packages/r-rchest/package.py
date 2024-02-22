# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchest(RPackage):
	"""Locating Distributional Changes in Highly Dependent Time Series

	Provides algorithms to locate multiple
    distributional change-points in piecewise stationary time series. The
    algorithms are provably consistent, even in the presence of long-range
    dependencies. Knowledge of the number of change-points is not
    required. The code is written in Go and interfaced with R.
	"""
	
	homepage = "https://github.com/azalk/GoChest"
	cran = "RChest" 

	version("1.0.3", md5="7f1396c139295f8ac1da814f704fc6ed")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
