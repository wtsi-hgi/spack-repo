# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebusBase(RPackage):
	"""Core Functionality for the 'rebus' Package

	Build regular expressions piece by piece using human readable code.
    This package contains core functionality, and is primarily intended to be
    used by package developers.
	"""
	
	homepage = "https://github.com/richierocks/rebus.base"
	cran = "rebus.base" 

	version("0.0-3", md5="20a5b5cfba098baadc034d067b5f8067")

	depends_on("r@3.1:", type=("build", "run"))
