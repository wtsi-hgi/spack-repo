# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratallo(RPackage):
	"""Optimum Sample Allocation in Stratified Sampling

	Functions in this package provide solution to classical problem in
  survey methodology - an optimum sample allocation in stratified sampling. In
  this context, the optimum allocation is in the classical Tschuprow-Neyman's
  sense and it satisfies additional lower or upper bounds restrictions imposed
  on sample sizes in strata. There are few different algorithms available to
  use, and one them is based on popular sample allocation method that applies
  Neyman allocation to recursively reduced set of strata.
  This package also provides the function that computes a solution to the
  minimum cost allocation problem, which is a minor modification of the
  classical optimum sample allocation. This problem lies in the determination
  of a vector of strata sample sizes that minimizes total cost of the survey,
  under assumed fixed level of the stratified estimator's variance. As in the
  case of the classical optimum allocation, the problem of minimum cost
  allocation can be complemented by imposing upper-bounds constraints on sample
  sizes in strata.
	"""
	
	homepage = "https://github.com/wwojciech/stratallo"
	cran = "stratallo" 

	version("2.2.1", md5="976808ea7ec700d3594b725f7d4d378c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
