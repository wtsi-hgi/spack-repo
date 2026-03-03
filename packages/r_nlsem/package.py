# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsem(RPackage):
	"""Fitting Structural Equation Mixture Models

	Estimation of structural equation models with nonlinear effects
  and underlying nonnormal distributions.
	"""
	
	homepage = "https://github.com/nwickel/nlsem"
	cran = "nlsem" 

	version("0.8-1", md5="c0d455e35f8eb7bfa9fafe38c3a3ba09")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-gaussquad", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
