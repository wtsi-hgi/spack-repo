# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWsrf(RPackage):
	"""Weighted Subspace Random Forest for Classification

	
    A parallel implementation of Weighted Subspace Random Forest.  The
    Weighted Subspace Random Forest algorithm was proposed in the
    International Journal of Data Warehousing and Mining by Baoxun Xu,
    Joshua Zhexue Huang, Graham Williams, Qiang Wang, and Yunming Ye
    (2012) <DOI:10.4018/jdwm.2012040103>.  The algorithm can classify
    very high-dimensional data with random forests built using small
    subspaces.  A novel variable weighting method is used for variable
    subspace selection in place of the traditional random variable
    sampling.This new approach is particularly useful in building
    models from high-dimensional data.
	"""
	
	homepage = "https://github.com/SimonYansenZhao/wsrf"
	cran = "wsrf" 

	version("1.7.30", md5="73bc81046c8f0c57915f0d1e5961938b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
