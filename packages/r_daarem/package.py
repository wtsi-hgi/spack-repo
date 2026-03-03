# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaarem(RPackage):
	"""Damped Anderson Acceleration with Epsilon Monotonicity for
Accelerating EM-Like Monotone Algorithms

	Implements the DAAREM method for accelerating the convergence of slow, monotone sequences from smooth, fixed-point iterations such as the EM algorithm. For further details about the DAAREM method, see Henderson, N.C. and Varadhan, R. (2019) <doi:10.1080/10618600.2019.1594835>.
	"""
	
	homepage = "https://doi.org/10.1080/10618600.2019.1594835"
	cran = "daarem" 

	version("0.7", md5="1561826b5177b970a01d64f29b0ef645")

