# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprobsup(RPackage):
	"""Calculates Probability of Superiority

	The A() function calculates the A statistic, a nonparametric
    measure of effect size for two independent groups that’s also known as
    the probability of superiority (Ruscio, 2008), along with its standard
    error and a confidence interval constructed using bootstrap methods 
    (Ruscio & Mullen, 2012). Optional arguments can be specified to 
    calculate variants of the A statistic developed for other research 
    designs (e.g., related samples, more than two independent groups or 
    related samples; Ruscio & Gera, 2013). 
    <DOI: 10.1037/1082-989X.13.1.19>.
    <DOI: 10.1080/00273171.2012.658329>.
    <DOI: 10.1080/00273171.2012.738184>.
	"""
	
	cran = "RProbSup" 

	version("3.0", md5="2de14eb65ee2f54b17a62c9a3522a919")

