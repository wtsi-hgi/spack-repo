# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMco(RPackage):
	"""Multiple Criteria Optimization Algorithms and Related Functions.

	A collection of function to solve multiple criteria optimization problems
	using genetic algorithms (NSGA-II). Also included is a collection of test
	functions."""

	cran = "mco"

	license("GPL-2.0-only")

	version("1.16", md5="7ff9cdd831212a225ef3a34876abeb4a")

	depends_on("r@3:", type=("build", "run"))
