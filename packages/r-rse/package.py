# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRse(RPackage):
	"""Number of Newly Discovered Rare Species Estimation

	A Bayesian-weighted estimator and two unweighted estimators are
 developed to estimate the number of newly found rare species in additional
 ecological samples. Among these methods, the Bayesian-weighted estimator
 and an unweighted (Chao-derived) estimator are of high accuracy and
 recommended for practical applications.
 Technical details of the proposed estimators have been well described
 in the following paper: Shen TJ, Chen YH (2018) A Bayesian
 weighted approach to predicting the number of newly discovered
 rare species. Conservation Biology, In press.
	"""
	
	cran = "RSE" 

	version("1.3", md5="edb2151e580606fb228ddb1274741d8c")

