# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebusNumbers(RPackage):
	"""Numeric Extensions for the 'rebus' Package

	Build regular expressions piece by piece using human readable code.
    This package contains number-related functionality, and is primarily intended
    to be used by package developers.
	"""
	
	cran = "rebus.numbers" 

	version("0.0-1", md5="bc896a0bbe0c0beacdf7e38875b80172")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rebus-base", type=("build", "run"))
