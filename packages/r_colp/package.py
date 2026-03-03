# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColp(RPackage):
	"""Causal Discovery for Categorical Data with Label Permutation

	Discover causality for bivariate categorical data. This package aims to enable users to discover causality for bivariate observational categorical data. See Ni, Y. (2022) <arXiv:2209.08579> "Bivariate Causal Discovery for Categorical Data via Classification with Optimal Label Permutation. Advances in Neural Information Processing Systems 35 (in press)".
	"""
	
	homepage = "https://github.com/nySTAT/COLP"
	cran = "COLP" 

	version("1.0.0", md5="1ff9a4384803e1978f6894923251fdce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
