# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultalloc(RPackage):
	"""Optimal Allocation in Stratified Sampling

	Integer Programming Formulations Applied to Univariate and Multivariate Allocation Problems.
	"""
	
	cran = "MultAlloc" 

	version("1.2", md5="249bb7d478dc601f76d1378925472bab")

	depends_on("r-rglpk", type=("build", "run"))
