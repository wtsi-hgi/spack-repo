# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCostsensitive(RPackage):
	"""Cost-Sensitive Multi-Class Classification

	Reduction-based techniques for cost-sensitive multi-class classification, in which each observation has a different cost for classifying it into one class, and the goal is to predict the class with the minimum expected cost for each new observation.
	Implements Weighted All-Pairs (Beygelzimer, A., Langford, J., & Zadrozny, B., 2008, <doi:10.1007/978-0-387-79361-0_1>), Weighted One-Vs-Rest (Beygelzimer, A., Dani, V., Hayes, T., Langford, J., & Zadrozny, B., 2005, <https://dl.acm.org/citation.cfm?id=1102358>) and Regression One-Vs-Rest.
	Works with arbitrary classifiers taking observation weights, or with regressors. Also implements cost-proportionate rejection sampling for working with classifiers
	that don't accept observation weights.
	"""
	
	homepage = "https://github.com/david-cortes/costsensitive"
	cran = "costsensitive" 

	version("0.1.2.10", md5="9a3a52e8e5c56c261838eba6e5a8096a")

