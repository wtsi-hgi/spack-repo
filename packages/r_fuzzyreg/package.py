# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyreg(RPackage):
	"""Fuzzy Linear Regression

	Estimators for fuzzy linear regression. The functions estimate parameters of 
    fuzzy linear regression models with crisp or fuzzy independent variables (triangular
    fuzzy numbers are supported). Implements multiple methods for parameter estimation and 
    algebraic operations with triangular fuzzy numbers. Includes functions for 
    summarising, printing and plotting the model fit. Calculates predictions from the 
    model and total error of fit. Individual methods are described in
    Diamond (1988) <doi:10.1016/0020-0255(88)90047-3>,
	Hung & Yang (2006) <doi:10.1016/j.fss.2006.08.004>,
	Lee & Tanaka (1999) <doi:10.15807/jorsj.42.98>,
	Nasrabadi, Nasrabadi & Nasrabady (2005) <doi:10.1016/j.amc.2004.02.008>,
	Skrabanek, Marek & Pozdilkova (2021) <doi:10.3390/math9060685>,
	Tanaka, Hayashi & Watada (1989) <doi:10.1016/0377-2217(89)90431-1>,
	Zeng, Feng & Li (2017) <doi:10.1016/j.asoc.2016.09.029>.
	"""
	
	cran = "fuzzyreg" 

	version("0.6.2", md5="0d546f08e93ba707ca323945bf2e3be4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
