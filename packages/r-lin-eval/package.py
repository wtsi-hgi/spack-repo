# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinEval(RPackage):
	"""Perform Polynomial Evaluation of Linearity

	Evaluates whether the relationship between two vectors is linear or nonlinear. Performs a test to determine how well a linear model fits the data compared to higher order polynomial models. Jhang et al. (2004) <doi:10.1043/1543-2165(2004)128%3C44:EOLITC%3E2.0.CO;2>.
	"""
	
	cran = "lin.eval" 

	version("0.1.2", md5="37e13932e69b4d7450be49800b8dd6d5")

	depends_on("r-broom", type=("build", "run"))
