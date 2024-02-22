# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighmean(RPackage):
	"""Two-Sample Tests for High-Dimensional Mean Vectors

	Provides various tests for comparing high-dimensional mean vectors in two sample populations.
	"""
	
	cran = "highmean" 

	version("3.0", md5="c9e96abea1be4f19be75ebd0b3966769")

	depends_on("r@1.9:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
