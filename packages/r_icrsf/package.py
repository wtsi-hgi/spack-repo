# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcrsf(RPackage):
	"""A Modified Random Survival Forest Algorithm

	Implements a modification to the Random Survival Forests algorithm for obtaining variable importance in high dimensional datasets. The proposed algorithm is appropriate for settings in which a silent event is observed through sequentially administered, error-prone self-reports or laboratory based diagnostic tests.  The modified algorithm incorporates a formal likelihood framework that accommodates sequentially administered, error-prone self-reports or laboratory based diagnostic tests. The original Random Survival Forests algorithm is modified by the introduction of a new splitting criterion based on a likelihood ratio test statistic.
	"""
	
	cran = "icRSF" 

	version("1.2", md5="dd11a75437913bb1677c0b7618d3b53d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-icensmis", type=("build", "run"))
