# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDovalidation(RPackage):
	"""Kernel Hazard Estimation with Best One-Sided and Double
One-Sided Cross-Validation

	Local linear hazard estimator and its multiplicatively bias correction, including three bandwidth selection methods: best one-sided cross-validation, double one-sided cross-validation, and standard cross-validation.
	"""
	
	cran = "DOvalidation" 

	version("1.1.0", md5="3bfb036a775802b5bbd2c2b2ff08ee73")

