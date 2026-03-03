# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlscpc(RPackage):
	"""Accelerated line search algorithm for simultaneous orthogonal
transformation of several positive definite symmetric matrices
to nearly diagonal form

	Using of the accelerated line search algorithm  for simultaneously diagonalize a set of symmetric positive definite matrices.
	"""
	
	cran = "ALSCPC" 

	version("1.0", md5="7271926d98bf85adfcb5277d38ff6291")

