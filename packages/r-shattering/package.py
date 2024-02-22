# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShattering(RPackage):
	"""Estimate the Shattering Coefficient for a Particular Dataset

	The Statistical Learning Theory (SLT) provides the theoretical background to ensure that a supervised algorithm generalizes the mapping f:X -> Y given f is selected from its search space bias F. This formal result depends on the Shattering coefficient function N(F,2n) to upper bound the empirical risk minimization principle, from which one can estimate the necessary training sample size to ensure the probabilistic learning convergence and, most importantly, the characterization of the capacity of F, including its under and overfitting abilities while addressing specific target problems. In this context, we propose a new approach to estimate the maximal number of hyperplanes required to shatter a given sample, i.e., to separate every pair of points from one another, based on the recent contributions by Har-Peled and Jones in the dataset partitioning scenario, and use such foundation to analytically compute the Shattering coefficient function for both binary and multi-class problems. As main contributions, one can use our approach to study the complexity of the search space bias F, estimate training sample sizes, and parametrize the number of hyperplanes a learning algorithm needs to address some supervised task, what is specially appealing to deep neural networks. Reference: de Mello, R.F. (2019) "On the Shattering Coefficient of Supervised Learning Algorithms" <arXiv:1911.05461>; de Mello, R.F., Ponti, M.A. (2018, ISBN: 978-3319949888) "Machine Learning: A Practical Approach on the Statistical Learning Theory".
	"""
	
	cran = "shattering" 

	version("1.0.7", md5="3a6bb96d8fca02aacde1abe46c302d94")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
