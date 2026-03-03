# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridot(RPackage):
	"""Approximate Optimal Transport Between Two-Dimensional Grids

	Can be used for optimal transport between two-dimensional grids with respect to separable cost functions of l^p form. It utilizes the Frank-Wolfe algorithm to approximate so-called pivot measures: one-dimensional transport plans that fully describe the full transport, see G. Auricchio (2021) <arXiv:2105.07278>. For these, it offers methods for visualization and to extract the corresponding transport plans and costs. Additionally, related functions for one-dimensional optimal transport are available.
	"""
	
	cran = "gridOT" 

	version("1.0.1", md5="ac0a6c077111add42cfb5502e09e4206")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
