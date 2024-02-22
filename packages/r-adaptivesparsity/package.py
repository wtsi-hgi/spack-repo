# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptivesparsity(RPackage):
	"""Adaptive Sparsity Models

	Implements Figueiredo EM algorithm for adaptive sparsity (Jeffreys prior) (see Figueiredo, M.A.T.; , "Adaptive sparseness for supervised learning," Pattern Analysis and Machine Intelligence, IEEE Transactions on , vol.25, no.9, pp. 1150- 1159, Sept. 2003) and Wong algorithm for adaptively sparse gaussian geometric models (see Wong, Eleanor, Suyash Awate, and P. Thomas Fletcher. "Adaptive Sparsity in Gaussian Graphical Models." In Proceedings of the 30th International Conference on Machine Learning (ICML-13), pp. 311-319. 2013.)
	"""
	
	cran = "AdaptiveSparsity" 

	version("1.6", md5="2117240389432710cdba18b9fab42645")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp@0.12.13:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.2:", type=("build", "run"))
