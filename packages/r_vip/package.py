# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVip(RPackage):
	"""Variable Importance Plots

	A general framework for constructing variable importance plots from 
  various types of machine learning models in R. Aside from some standard model-
  specific variable importance measures, this package also provides model-
  agnostic approaches that can be applied to any supervised learning algorithm.
  These include 1) an efficient permutation-based variable importance measure, 
  2) variable importance based on Shapley values (Strumbelj and Kononenko, 
  2014) <doi:10.1007/s10115-013-0679-x>, and 3) the variance-based 
  approach described in Greenwell et al. (2018) <arXiv:1805.04755>. A 
  variance-based method for quantifying the relative strength of interaction 
  effects is also included (see the previous reference for details).
	"""
	
	homepage = "https://github.com/koalaverse/vip/"
	cran = "vip" 

	version("0.4.1", md5="107ee00bd6c7ebc7f2785608e67c645f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@0.9:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yardstick", type=("build", "run"))
