# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxstat(RPackage):
	"""Maximally Selected Rank Statistics

	Maximally selected rank statistics with
 several p-value approximations.
	"""
	
	cran = "maxstat" 

	version("0.7-25", md5="35b234371e4321d98e7659d2f3a35546")

	depends_on("r@1.7:", type=("build", "run"))
	depends_on("r-exactranktests@0.8.23:", type=("build", "run"))
	depends_on("r-mvtnorm@0.5.10:", type=("build", "run"))
