# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzysts(RPackage):
	"""Fuzzy Statistical Tools

	The main goal of this package is to present various fuzzy statistical tools. It intends to provide an implementation of the theoretical and empirical approaches presented in the thesis entitled "The signed distance measure in fuzzy statistical analysis. Some theoretical, empirical and programming advances" (Thesis to be published soon. For the theoretical approaches, see Berkachy R. and Donze L. (2019) <doi:10.1007/978-3-030-03368-2_1>. For the empirical approaches, see Berkachy R. and Donze L. (2016) <ISBN: 978-989-758-201-1>). Important (non-exhaustive) implementation highlights of this package are as follows: (1) a numerical procedure to estimate the fuzzy difference and the fuzzy square. (2) two numerical methods of fuzzification. (3) a function performing different possibilities of distances, including the signed distance and the generalized signed distance for instance. (4) numerical estimations of fuzzy statistical measures such as the variance, the moment, etc. (5) two methods of estimation of the bootstrap distribution of the likelihood ratio in the fuzzy context. (6) an estimation of a fuzzy confidence interval by the likelihood ratio method. (7) testing fuzzy hypotheses and/or fuzzy data by fuzzy confidence intervals in the Kwakernaak - Kruse and Meyer sense. (8) a general method to estimate the fuzzy p-value with fuzzy hypotheses and/or fuzzy data. (9) a method of estimation of global and individual evaluations of linguistic questionnaires. (10) numerical estimations of multi-ways analysis of variance models in the fuzzy context. The unbalance in the considered designs are also foreseen. 
	"""
	
	cran = "FuzzySTs" 

	version("0.2", md5="9f529e1821f27f5a29a46ede5683df9c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fuzzynumbers", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
