# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsallisqexp(RPackage):
	"""Tsallis q-Exp Distribution

	Tsallis distribution also known as the q-exponential family distribution. Provide distribution d, p, q, r functions, fitting and testing functions. Project initiated by Paul Higbie and based on Cosma Shalizi's code.
	"""
	
	cran = "tsallisqexp" 

	version("0.9-4", md5="6668d3746d165a96257e71444a200ba2")

	depends_on("r@3:", type=("build", "run"))
