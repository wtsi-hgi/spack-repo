# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpe(RPackage):
	"""Concordance Probability Estimates in Survival Analysis

	Concordance probability estimate (CPE) is a commonly used performance measure in survival analysis that evaluates the predictive accuracy of a survival model.  It measures how well a model can distinguish between pairs of individuals with different survival times.  Specifically, it calculate the proportion of all pairs of individuals whose predicted survival times are correctly ordered.
	"""
	
	cran = "CPE" 

	version("1.6.3", md5="b7cb50baea175b4aaf590933325b8848")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
