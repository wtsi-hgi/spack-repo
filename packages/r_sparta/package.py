# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparta(RPackage):
	"""Sparse Tables

	Fast Multiplication and Marginalization of Sparse Tables.
	"""
	
	homepage = "https://github.com/mlindsk/sparta"
	cran = "sparta" 

	version("0.8.4", md5="b71220d2689b2fe72859c6b0b72fe644")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
