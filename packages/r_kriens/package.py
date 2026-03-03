# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKriens(RPackage):
	"""Continuation Passing Style Development

	Provides basic functions for Continuation-Passing Style development.
	"""
	
	homepage = "http://www.alephdue.com"
	cran = "kriens" 

	version("0.1", md5="1a5e86e0b7e0042cf59fe364b09b8d81")

