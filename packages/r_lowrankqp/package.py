# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLowrankqp(RPackage):
	"""Low Rank Quadratic Programming

	Solves quadratic programming problems where the Hessian is represented as the product of two matrices. Thanks to Greg Hunt for helping getting this version back on CRAN. The methods in this package are described in: Ormerod, Wand and Koch (2008) "Penalised spline support vector classifiers: computational issues" <doi:10.1007/s00180-007-0102-8>.
	"""
	
	cran = "LowRankQP" 

	version("1.0.6", md5="719952173d35a5053d8d40a6e58dcbf7")

