# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmmsslm(RPackage):
	"""Semi-Supervised Gaussian Mixture Model with a Missing-Data
Mechanism

	The algorithm of semi-supervised learning is based on finite Gaussian mixture models and includes a mechanism for handling missing data. It aims to fit a g-class Gaussian mixture model using maximum likelihood. The algorithm treats the labels of unclassified features as missing data, building on the framework introduced by Rubin (1976) <doi:10.2307/2335739> for missing data analysis. By taking into account the dependencies in the missing pattern, the algorithm provides more information for determining the optimal classifier, as specified by Bayes' rule.
	"""
	
	cran = "gmmsslm" 

	version("1.1.5", md5="d29ac3780159328ca0eabbe78c772cba")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
