# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtsspec(RPackage):
	"""Spectral Density Estimation and Comparison for Functional Time
Series

	Functions for estimating spectral density operator of functional
    time series (FTS) and comparing the spectral density operator of two
    functional time series, in a way that allows detection of differences of
    the spectral density operator in frequencies and along the curve length.
	"""
	
	cran = "ftsspec" 

	version("1.0.0", md5="d1019cdb470772d648459d10f147133a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sna@2.3.2:", type=("build", "run"))
