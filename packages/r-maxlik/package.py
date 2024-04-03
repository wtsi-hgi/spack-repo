# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxlik(RPackage):
	"""Maximum Likelihood Estimation and Related Tools

	Functions for Maximum Likelihood (ML) estimation, non-linear
   optimization, and related tools.  It includes a unified way to call
   different optimizers, and classes and methods to handle the results from
   the Maximum Likelihood viewpoint.  It also includes a number of convenience
   tools for testing and developing your own models.
	"""
	
	cran = "maxLik" 

	version("1.5-2.1", md5="e323d471779aee086abc6d7771701258")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-misctools@0.6.8:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
