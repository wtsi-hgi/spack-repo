# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDblcens(RPackage):
	"""Compute the NPMLE of Distribution Function from Doubly Censored
Data, Plus the Empirical Likelihood Ratio for F(T)

	Doubly censored data, as described in Chang and Yang (1987) <doi: 10.1214/aos/1176350608>), are commonly seen in many fields. We use EM algorithm to compute the non-parametric MLE (NPMLE) of the cummulative probability function/survival function and the two censoring distributions. One can also specify a constraint F(T)=C, it will return the constrained NPMLE and the -2 log empirical likelihood ratio for this constraint. This can be used to test the hypothesis about the constraint and, by inverting the test, find confidence intervals for probability or quantile via empirical likelihood ratio theorem. Influence functions of hat F may also be calculated, but currently, the it may be slow.
	"""
	
	homepage = "https://github.com/yfyang86/dblcens/"
	cran = "dblcens" 

	version("1.1.9", md5="f63369d7c27f437d514fe01902aabbd8")

	depends_on("r@3.5:", type=("build", "run"))
