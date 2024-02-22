# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiv(RPackage):
	"""Robust Instrumental Variables Estimator

	Finds a robust instrumental variables estimator using a
             high breakdown point S-estimator of multivariate location
             and scatter matrix.
	"""
	
	cran = "riv" 

	version("2.0-5", md5="9d7840a99a3c78cdf9fcf3d2e53be02e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
