# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlbstats(RPackage):
	"""Major League Baseball Player Statistics Calculator

	Computational functions for player metrics in major league baseball including batting, pitching, fielding, base-running, and overall player statistics. This package is actively maintained with new metrics being added as they are developed.
	"""
	
	cran = "mlbstats" 

	version("0.1.0", md5="aec4db6d59d4533695497975ec905415")

