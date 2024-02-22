# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhaz(RPackage):
	"""Regularization for Semiparametric Additive Hazards Regression

	Computationally efficient procedures for regularized
        estimation with the semiparametric additive hazards regression
        model.
	"""
	
	cran = "ahaz" 

	version("1.15", md5="e449b6904ecc34ae2bf47805205335f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
