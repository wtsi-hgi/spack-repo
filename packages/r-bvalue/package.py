# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvalue(RPackage):
	"""B-Value and Empirical Equivalence Bound

	Calculates B-value and empirical equivalence bound. B-value is defined as the maximum magnitude of a confidence interval; and the empirical equivalence bound is the minimum B-value at a certain level. A new two-stage procedure for hypothesis testing is proposed, where the first stage is conventional hypothesis testing and the second is an equivalence testing procedure using the introduced empirical equivalence bound. See Zhao et al. (2019) "B-Value and Empirical Equivalence Bound: A New Procedure of Hypothesis Testing" <arXiv:1912.13084> for details.
	"""
	
	cran = "Bvalue" 

	version("1.0", md5="44b40dad5d96ef1af15cfc78a23af34a")

