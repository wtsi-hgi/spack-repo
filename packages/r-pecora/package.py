# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPecora(RPackage):
	"""Permutation Conditional Random Tests

	It provides functions to perform permutation conditional random one-sample and two-samples t-tests in a multivariate framework.
	"""
	
	cran = "pecora" 

	version("0.1.1", md5="f42e13d60b3b6703dcbab3854065a608")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
