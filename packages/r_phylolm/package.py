# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylolm(RPackage):
	"""Phylogenetic Linear Regression

	Provides functions for fitting phylogenetic linear models and phylogenetic generalized linear models. The computation uses an algorithm that is linear in the number of tips in the tree. The package also provides functions for simulating continuous or binary traits along the tree. Other tools include functions to test the adequacy of a population tree.
	"""
	
	homepage = "https://github.com/lamho86/phylolm"
	cran = "phylolm" 

	version("2.6.2", md5="83d563e140739398ae32c530e32272b1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
