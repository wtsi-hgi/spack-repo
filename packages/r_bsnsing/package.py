# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsnsing(RPackage):
	"""Build Decision Trees with Optimal Multivariate Splits

	Functions for training an optimal decision tree classifier, making predictions and generating latex code for plotting. Works for two-class and multi-class classification problems. The algorithm seeks the optimal Boolean rule consisting of multiple variables to split a node, resulting in shorter trees. Use bsnsing() to build a tree, predict() to make predictions and plot() to plot the tree into latex and PDF. See Yanchao Liu (2022) <arXiv:2205.15263> for technical details. Source code and more data sets are at <https://github.com/profyliu/bsnsing/>.
	"""
	
	cran = "bsnsing" 

	version("1.0.1", md5="612ce01d93cf5229452fda0283ac5bf7")

	depends_on("r-rcpp", type=("build", "run"))
