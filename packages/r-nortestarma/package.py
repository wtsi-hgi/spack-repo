# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNortestarma(RPackage):
	"""Neyman Smooth Tests of Normality for the Errors of ARMA Models

	Tests the goodness-of-fit to the Normal distribution for the errors of an ARMA model.
	"""
	
	cran = "nortestARMA" 

	version("1.0.2", md5="0726182b99bab6a1f8b59c71f14b8e83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
