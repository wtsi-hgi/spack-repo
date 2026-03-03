# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcg(RPackage):
	"""Preconditioned Conjugate Gradient Algorithm for solving Ax=b

	The package solves linear system of equations Ax=b by using Preconditioned Conjugate Gradient Algorithm where A is real symmetric positive definite matrix. A suitable preconditioner matrix may be provided by user. This can also be used to minimize quadratic function (x'Ax)/2-bx for unknown x.
	"""
	
	cran = "pcg" 

	version("1.1", md5="f32af5161ac230c439090681bd06b16a")

