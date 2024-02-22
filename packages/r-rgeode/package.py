# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgeode(RPackage):
	"""Geometric Density Estimation

	Provides the hybrid Bayesian method Geometric Density Estimation. On the one hand, it scales the dimension of our data, on the other it performs inference. The method is fully described in the paper "Scalable Geometric Density Estimation" by Y. Wang, A. Canale, D. Dunson (2016) <http://proceedings.mlr.press/v51/wang16e.pdf>.                   
	"""
	
	cran = "RGeode" 

	version("0.1.0", md5="4a056207742ec07d48f816e2cb5c1637")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
