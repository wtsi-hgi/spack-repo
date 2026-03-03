# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeEq(RPackage):
	"""SE-Test for Equivalence

	Implements the SE-test for equivalence
    according to Hoffelder et al. (2015) <DOI:10.1080/10543406.2014.920344>.
    The SE-test for equivalence is a multivariate two-sample equivalence test. 
    Distance measure of the test is the sum of standardized differences
    between the expected values or in other words: the sum of effect sizes (SE)
    of all components of the two multivariate samples. 
    The test is an asymptotically valid test for normally distributed data 
    (see Hoffelder et al.,2015).
    The function SE.EQ() implements the SE-test for equivalence 
    according to Hoffelder et al. (2015).
    The function SE.EQ.dissolution.profiles() implements a variant 
    of the SE-test for equivalence for similarity analyses of dissolution 
    profiles as mentioned in Suarez-Sharp et al.(2020) 
    <DOI:10.1208/s12248-020-00458-9>). The equivalence margin used in 
    SE.EQ.dissolution.profiles() is analogically defined as for the T2EQ
    approach according to Hoffelder (2019) <DOI:10.1002/bimj.201700257>) 
    by means of a systematic shift in location
    of 10 [% of label claim] of both dissolution profile populations. 
    SE.EQ.dissolution.profiles() checks whether the weighted mean of the 
    differences of the expected values of both dissolution profile populations 
    is statistically significantly smaller than 10 [% of label claim]. The 
    weights are built up by the inverse variances.
	"""
	
	cran = "SE.EQ" 

	version("1.0", md5="f6cf00e8f75cafb9d74b6038e4974837")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
