# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBagoft(RPackage):
	"""A Binary Regression Adaptive Goodness-of-Fit Test (BAGofT)

	The BAGofT assesses the goodness-of-fit of binary classifiers. Details can be found in Zhang, Ding and Yang (2021) <arXiv:1911.03063v2>.
	"""
	
	cran = "BAGofT" 

	version("1.0.0", md5="8c3e6877ce260ca6401a7fc318bdb7a9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-dcov@0.1.1:", type=("build", "run"))
