# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiglmm(RPackage):
	"""Bounded Memory Linear and Generalized Linear Models

	Regression for data too large to fit in memory. This package functions exactly like the 'biglm' package, but works with later versions of R.
	"""
	
	cran = "biglmm" 

	version("0.9-2", md5="4b1cadfa8ae281214cd96d806fdc5ab2")

	depends_on("r-dbi", type=("build", "run"))
