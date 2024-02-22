# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidylo(RPackage):
	"""Weighted Tidy Log Odds Ratio

	How can we measure how the usage or frequency of some
    feature, such as words, differs across some group or set, such as
    documents? One option is to use the log odds ratio, but the log odds
    ratio alone does not account for sampling variability; we haven't
    counted every feature the same number of times so how do we know which
    differences are meaningful? Enter the weighted log odds, which
    'tidylo' provides an implementation for, using tidy data principles.
    In particular, here we use the method outlined in Monroe, Colaresi,
    and Quinn (2008) <doi:10.1093/pan/mpn018> to weight the log odds ratio
    by a prior. By default, the prior is estimated from the data itself,
    an empirical Bayes approach, but an uninformative prior is also
    available.
	"""
	
	homepage = "https://juliasilge.github.io/tidylo/"
	cran = "tidylo" 

	version("0.2.0", md5="94f2663c5ab585701f83f5f905bc6ac8")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
