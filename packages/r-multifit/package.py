# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifit(RPackage):
	"""Multiscale Fisher's Independence Test for Multivariate
Dependence

	Test for independence of two random vectors, learn and report the dependency structure. For more information, see Gorsky, Shai and Li Ma, Multiscale Fisher's Independence Test for Multivariate Dependence, Biometrika, accepted, January 2022.
	"""
	
	cran = "MultiFit" 

	version("1.1.1", md5="b2ee42e923788518c482f000811c3f3f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
