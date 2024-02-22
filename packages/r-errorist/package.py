# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErrorist(RPackage):
	"""Automatically Search Errors or Warnings

	Provides environment hooks that obtain errors and warnings which
    occur during the execution of code to automatically search for solutions.
	"""
	
	homepage = "https://github.com/coatless-rpkg/errorist"
	cran = "errorist" 

	version("0.1.2", md5="0cc07d211906110c74a17a22947c5503")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-searcher@0.0.2:", type=("build", "run"))
