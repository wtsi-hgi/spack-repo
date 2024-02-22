# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoubcens(RPackage):
	"""Survivor Function Estimation for Doubly Interval-Censored
Failure Time Data

	Contains the discrete nonparametric survivor function estimation algorithm of De Gruttola and Lagakos for doubly interval-censored failure time data and the discrete nonparametric survivor function estimation algorithm of Sun for doubly interval-censored left-truncated failure time data [Victor De Gruttola  & Stephen W. Lagakos (1989) <doi:10.2307/2532030>] [Jianguo Sun (1995) <doi:10.2307/2533008>].  
	"""
	
	cran = "doubcens" 

	version("1.1", md5="db9ced2981fe5c9949e395347df1545d")

	depends_on("r@3.1.1:", type=("build", "run"))
