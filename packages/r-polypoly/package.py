# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolypoly(RPackage):
	"""Helper Functions for Orthogonal Polynomials

	Tools for reshaping, plotting, and manipulating matrices of orthogonal polynomials.
	"""
	
	homepage = "https://github.com/tjmahr/polypoly"
	cran = "polypoly" 

	version("0.0.3", md5="b2698c8a7995dfa3dea34148e7cbc837")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
