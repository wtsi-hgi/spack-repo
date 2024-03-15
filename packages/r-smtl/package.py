# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmtl(RPackage):
	"""Sparse Multi-Task Learning

	Implements L0-constrained Multi-Task Learning and domain generalization algorithms. The algorithms are coded in Julia allowing for fast implementations of the coordinate descent and local combinatorial search algorithms. For more details, see a preprint of the paper: Loewinger et al., (2022) <arXiv:2212.08697>.
	"""
	
	homepage = "https://github.com/gloewing/sMTL"
	cran = "sMTL" 

	version("0.1.0", md5="02164a319ad58f910cc2a944c731052a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-juliacall", type=("build", "run"))
	depends_on("r-juliaconnector", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
