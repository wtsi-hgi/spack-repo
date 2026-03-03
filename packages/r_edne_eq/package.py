# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdneEq(RPackage):
	"""Implements the EDNE-Test for Equivalence

	Package implements the EDNE-test for equivalence
    according to Hoffelder et al. (2015) <DOI:10.1080/10543406.2014.920344>.
    "EDNE" abbreviates "Euclidean Distance between the 
    Non-standardized Expected values".
    The EDNE-test for equivalence is a multivariate two-sample equivalence test. 
    Distance measure of the test is the Euclidean distance.
    The test is an asymptotically valid test for the family of distributions 
    fulfilling the assumptions of the multivariate central limit theorem 
    (see Hoffelder et al.,2015).
    The function EDNE.EQ() implements the EDNE-test for equivalence 
    according to Hoffelder et al. (2015).
    The function EDNE.EQ.dissolution.profiles() implements a variant 
    of the EDNE-test for equivalence analyses of dissolution profiles
    (see Suarez-Sharp et al.,2020 <DOI:10.1208/s12248-020-00458-9>).
    EDNE.EQ.dissolution.profiles() checks whether the quadratic mean of the 
    differences of the expected values of both dissolution profile populations 
    is statistically significantly smaller than 10 [% of label claim]. 
    The current regulatory standard approach for equivalence analyses of 
    dissolution profiles is the similarity factor f2.
    The statistical hypotheses underlying EDNE.EQ.dissolution.profiles()
    coincide with the hypotheses for f2 (see Hoffelder et al.,2015, 
    Suarez-Sharp et al., 2020).
	"""
	
	cran = "EDNE.EQ" 

	version("1.0", md5="8015a6e19d6b4736bc5a5919cca257f2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
