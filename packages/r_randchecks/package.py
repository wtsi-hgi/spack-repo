# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandchecks(RPackage):
	"""Covariate Balance Checks: Randomization Tests and Graphical
Diagnostics

	Provides randomization tests and graphical diagnostics for assessing randomized assignment and covariate balance for a binary treatment variable. See Branson (2021) <arXiv:1804.08760> for details.
	"""
	
	cran = "randChecks" 

	version("0.2.1", md5="61516ad7aee20b4aa68552b97064d1ac")

	depends_on("r@3.5:", type=("build", "run"))
