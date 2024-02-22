# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNorma(RPackage):
	"""Builds General Noise SVRs

	Builds general noise SVR models using Naive Online R Minimization Algorithm, NORMA, an optimization method based on classical stochastic gradient descent suitable for computing SVR models in an online setting.
	"""
	
	homepage = "http://link.springer.com/chapter/10.1007/978-3-319-19222-2_47"
	cran = "NORMA" 

	version("0.1", md5="5959c1281c45ef69bcfe513cb18f608b")

	depends_on("r-rootsolve", type=("build", "run"))
