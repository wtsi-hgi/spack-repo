# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactcione(RPackage):
	"""Admissible Exact Intervals for One-Dimensional Discrete
Distributions

	Construct the admissible exact intervals for the binomial proportion, the Poisson mean and the total number of subjects with a certain attribute or the total number of the subjects for the hypergeometric distribution. Both one-sided and two-sided intervals are of interest. This package can be used to calculate the intervals constructed methods developed by Wang (2014) <doi:10.5705/ss.2012.257> and Wang (2015) <doi:10.1111/biom.12360>.
	"""
	
	cran = "ExactCIone" 

	version("1.0.0", md5="3b92e8213adbd6ddc4e6d694fd4c413c")
	version("1.0.5", md5="adf433017b55bd99aa0edb339e53bf31")

