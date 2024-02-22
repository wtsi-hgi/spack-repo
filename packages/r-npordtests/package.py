# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpordtests(RPackage):
	"""Nonparametric Tests for Equality of Location Against Ordered
Alternatives

	Performs nonparametric tests for equality of location against ordered alternatives. 
	"""
	
	cran = "npordtests" 

	version("1.2", md5="1a65d6858e999ed22b20dc310747d2d6")

	depends_on("r@3.5:", type=("build", "run"))
