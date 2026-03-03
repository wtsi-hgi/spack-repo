# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadr(RPackage):
	"""Model Averaged Double Robust Estimation

	Estimates average treatment effects using model average double robust (MA-DR) estimation. The MA-DR estimator is defined as weighted average of double robust estimators, where each double robust estimator corresponds to a specific choice of the outcome model and the propensity score model. The MA-DR estimator extend the desirable double robustness property by achieving consistency under the much weaker assumption that either the true propensity score model or the true outcome model be within a specified, possibly large, class of models.
	"""
	
	cran = "madr" 

	version("1.0.0", md5="9736ae4156099b2d14499369c5ce2581")

