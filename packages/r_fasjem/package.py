# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasjem(RPackage):
	"""A Fast and Scalable Joint Estimator for Learning Multiple
Related Sparse Gaussian Graphical Models

	This is an R implementation of "A Fast and Scalable Joint Estimator for Learning Multiple Related Sparse Gaussian Graphical Models" (FASJEM). The FASJEM algorithm can be used to estimate multiple related precision matrices. For instance, it can identify context-specific gene networks from multi-context gene expression datasets. By performing data-driven network inference from high-dimensional and heterogonous data sets, this tool  can help users effectively translate aggregated data into knowledge that take the form of graphs among entities. Please run demo(fasjem) to learn the basic functions provided by this package. For more details, please see <http://proceedings.mlr.press/v54/wang17e/wang17e.pdf>.
	"""
	
	homepage = "https://github.com/QData/JEM"
	cran = "fasjem" 

	version("1.1.2", md5="385114d94b27764aaa7dfc7518adff57")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
