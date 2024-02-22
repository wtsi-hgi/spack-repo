# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKere(RPackage):
	"""Expectile Regression in Reproducing Kernel Hilbert Space

	An efficient algorithm inspired by majorization-minimization principle for solving the entire solution path of a flexible nonparametric expectile regression estimator constructed in a reproducing kernel Hilbert space.
	"""
	
	cran = "KERE" 

	version("1.0.0", md5="8e8db35bde696d4e8134a3ccfc8e3717")

