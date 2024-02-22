# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptr(RPackage):
	"""Optimization Toolbox for Solving Linear Systems

	Solves linear systems of form Ax=b via Gauss elimination, 
  LU decomposition, Gauss-Seidel, Conjugate Gradient Method (CGM) and Cholesky methods.
	"""
	
	cran = "optR" 

	version("1.2.5", md5="4adb723e8202bf24eb07212db435e0d8")

