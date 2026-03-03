# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNilde(RPackage):
	"""Nonnegative Integer Solutions of Linear Diophantine Equations
with Applications

	Routines for enumerating all existing nonnegative integer solutions of a linear Diophantine equation. The package provides routines for solving 0-1, bounded and unbounded knapsack problems; 0-1, bounded and unbounded subset sum problems; additive partitioning of natural numbers; and one-dimensional bin-packing problem.
	"""
	
	cran = "nilde" 

	version("1.1-7", md5="3a23251fedd5158401d7adf14ba6e8d1")

	depends_on("r@2.15:", type=("build", "run"))
