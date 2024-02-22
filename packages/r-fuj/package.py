# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuj(RPackage):
	"""Functions and Utilities for Jordan

	Provides core functions and utilities for packages and other code
    developed by Jordan Mark Barbone.
	"""
	
	homepage = "https://jmbarbone.github.io/fuj/"
	cran = "fuj" 

	version("0.1.4", md5="34c00fb6d0fbe031ceb0f7d5f1598f28")

	depends_on("r@3.6:", type=("build", "run"))
