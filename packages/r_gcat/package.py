# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcat(RPackage):
	"""Graph-Based Two-Sample Tests for Categorical Data

	These are two-sample tests for categorical data utilizing similarity information among the categories.  They are useful when there is underlying structure on the categories.
	"""
	
	cran = "gCat" 

	version("0.2", md5="91c83ba56cff7b3b26e06a11bda06109")

	depends_on("r@3.0.1:", type=("build", "run"))
