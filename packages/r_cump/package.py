# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCump(RPackage):
	"""Analyze Multivariate Phenotypes by Combining Univariate Results

	Combining Univariate Association Test Results of Multiple Phenotypes for Detecting Pleiotropy.
	"""
	
	cran = "CUMP" 

	version("2.0", md5="1a95e71e71ae592234fa421e3126586a")

