# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocpol(RPackage):
	"""Kernel Local Polynomial Regression

	Computes local polynomial estimators for 
  the regression and also density. It comprises several 
  different utilities to handle kernel estimators.
	"""
	
	cran = "locpol" 

	version("0.8.0", md5="49308d0b46de409468fdaaf508eb48d4")

	depends_on("r@2.5:", type=("build", "run"))
