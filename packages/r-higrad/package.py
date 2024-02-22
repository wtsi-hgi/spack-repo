# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHigrad(RPackage):
	"""Statistical Inference for Online Learning and Stochastic
Approximation via HiGrad

	Implements the Hierarchical Incremental GRAdient Descent (HiGrad) algorithm,
    a first-order algorithm for finding the minimizer of a function in online learning just like stochastic gradient descent (SGD).
    In addition, this method attaches a confidence interval to assess the uncertainty of its predictions.
    See Su and Zhu (2018) <arXiv:1802.04876> for details. 
	"""
	
	cran = "higrad" 

	version("0.1.0", md5="93a34b740f17d7dfdd562b2ec1035651")

	depends_on("r-matrix", type=("build", "run"))
