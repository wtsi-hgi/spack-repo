# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLagsequential(RPackage):
	"""Lag-Sequential Categorical Data Analysis

	Lag-sequential analysis is a method of assessing of patterns (what tends to 
        follow what?) in sequences of codes. The codes are typically for discrete 
        behaviors or states. The functions in this package read a stream of codes,
        or a frequency transition matrix, and produce a variety of lag sequential  
        statistics, including transitional frequencies, expected transitional frequencies, 
        transitional probabilities, z values, adjusted residuals, Yule's Q values, 
        likelihood ratio tests of stationarity across time and homogeneity across groups 
        or segments, transformed kappas for unidirectional dependence, bidirectional 
        dependence, parallel and nonparallel dominance, and significance levels based on 
        both parametric and randomization tests. The methods are described in
  Bakeman & Quera (2011) <doi:10.1017/CBO9781139017343>,
  O'Connor (1999) <doi:10.3758/BF03200753>,
  Wampold & Margolin (1982) <doi:10.1037/0033-2909.92.3.755>, and
  Wampold (1995, ISBN:0-89391-919-5).
	"""
	
	cran = "LagSequential" 

	version("0.1.1", md5="45f5c7d1bc282a1944683f11f4092d3d")

	depends_on("r@1.9:", type=("build", "run"))
