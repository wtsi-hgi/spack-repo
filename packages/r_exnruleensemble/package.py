# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExnruleensemble(RPackage):
	"""A k Nearest Neibour Ensemble Based on Extended Neighbourhood
Rule

	The extended neighbourhood rule for the k nearest neighbour ensemble where the neighbours are determined in k steps. Starting from the first nearest observation of the test point, the algorithm identifies a single observation that is closest to the observation at the previous step. At each base learner in the ensemble, this search is extended to k steps on a random bootstrap sample with a random subset of features selected from the feature space. The final predicted class of the test point is determined by using a majority vote in the predicted classes given by all base models. Amjad Ali, Muhammad Hamraz, Naz Gul, Dost Muhammad Khan, Saeed Aldahmani, Zardad Khan (2022) <doi:10.48550/arXiv.2205.15111>.
	"""
	
	cran = "ExNRuleEnsemble" 

	version("0.1.1", md5="c670cf0a98c70011caf9edc5186b6dd4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
