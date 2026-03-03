# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkvo(RPackage):
	"""Read Key/Value Pair Observations

	This package provides functionality to read files
    containing observations which consist of arbitrary key/value
    pairs.
	"""
	
	cran = "rkvo" 

	version("0.1", md5="bc90bcf7a3a119e6f3e2d8d5964d19b2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
