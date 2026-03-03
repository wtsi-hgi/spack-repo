# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJeek(RPackage):
	"""A Fast and Scalable Joint Estimator for Integrating Additional
Knowledge in Learning Multiple Related Sparse Gaussian
Graphical Models

	Provides a fast and scalable joint estimator for integrating additional knowledge in learning multiple related sparse Gaussian Graphical Models (JEEK). The JEEK algorithm can be used to fast estimate multiple related precision matrices in a large-scale. For instance, it can identify multiple gene networks from multi-context gene expression datasets. By performing data-driven network inference from high-dimensional and heterogeneous data sets, this tool can help users effectively translate aggregated data into knowledge that take the form of graphs among entities. Please run demo(jeek) to learn the basic functions provided by this package. For further details, please read the original paper: Beilun Wang, Arshdeep Sekhon, Yanjun Qi "A Fast and Scalable Joint Estimator for Integrating Additional Knowledge in Learning Multiple Related Sparse Gaussian Graphical Models" (ICML 2018) <arXiv:1806.00548>.
	"""
	
	homepage = "https://github.com/QData/jeek"
	cran = "jeek" 

	version("1.1.1", md5="3aaa27b2bcc87459a8a96baddb3285c5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
