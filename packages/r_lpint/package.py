# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpint(RPackage):
	"""Local Polynomial Estimators of the Intensity Function and Its
Derivatives

	Functions to estimate the intensity function and its derivative of a given order of a multiplicative counting process using the local polynomial method.
	"""
	
	cran = "lpint" 

	version("2.1", md5="84d4fbf799def49f1de99d08be9b8c1d")

