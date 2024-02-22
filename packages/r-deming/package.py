# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeming(RPackage):
	"""Deming, Theil-Sen, Passing-Bablock and Total Least Squares
Regression

	Generalized Deming regression, Theil-Sen regression and Passing-Bablock regression functions.
	"""
	
	cran = "deming" 

	version("1.4", md5="d63daf672291763deca4518eb39f7be2")

	depends_on("r-boot", type=("build", "run"))
