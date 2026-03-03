# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacart(RPackage):
	"""Meta-CART: A Flexible Approach to Identify Moderators in
Meta-Analysis

	Meta-CART integrates classification and regression trees (CART) into meta-analysis. Meta-CART is a flexible approach to identify interaction effects between moderators in meta-analysis. The method is described in Dusseldorp et al. (2014) <doi:10.1037/hea0000018> and Li et al. (2017) <doi:10.1111/bmsp.12088>.
	"""
	
	cran = "metacart" 

	version("2.0-3", md5="8602d61c18a598a9d7a80583b8f5948b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
