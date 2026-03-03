# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovrobust(RPackage):
	"""Robust Covariance Estimation via Nearest Neighbor Cleaning

	The cov.nnve() function implements robust covariance estimation
        by the nearest neighbor variance estimation (NNVE) method of
        Wang and Raftery (2002) <DOI:10.1198/016214502388618780>.
	"""
	
	cran = "covRobust" 

	version("1.1-3", md5="458f8fb0ece3e294b14ac463667d27de")

	depends_on("r@2.15.1:", type=("build", "run"))
