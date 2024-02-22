# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringstatic(RPackage):
	"""Dependency-Free String Operations

	Provides drop-in replacements for functions from the
    'stringr' package, with the same user interface. These functions have
    no external dependencies and can be copied directly into your package
    code using the 'staticimports' package.
	"""
	
	homepage = "https://github.com/rossellhayes/stringstatic"
	cran = "stringstatic" 

	version("0.1.2", md5="cafd150f42880b7d03b2e2910cfb1612")

