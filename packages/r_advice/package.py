# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdvice(RPackage):
	"""Automatic Direct Variable Selection via Interrupted Coefficient
Estimation

	Accurate point and interval estimation methods for multiple linear regression coefficients, under classical normal and independent error assumptions, taking into account variable selection.   
	"""
	
	cran = "ADVICE" 

	version("1.0", md5="986b9823f2591e0b2e68e58474385102")

	depends_on("r@2.0.1:", type=("build", "run"))
