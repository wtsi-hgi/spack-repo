# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWpkde(RPackage):
	"""Weighted Piecewise Kernel Density Estimation

	Weighted Piecewise Kernel Density Estimation for large data.
	"""
	
	cran = "WPKDE" 

	version("0.1", md5="21e69786b00f8ec36ab19aa1aa2039bc")

