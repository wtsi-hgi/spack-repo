# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RT2eq(RPackage):
	"""Functions for Applying the T^2-Test for Equivalence

	Contains functions for applying the T^2-test for equivalence.
    The T^2-test for equivalence is a multivariate two-sample equivalence test. 
    Distance measure of the test is the Mahalanobis distance.
    For multivariate normally distributed data the T^2-test for equivalence 
    is exact and UMPI.
    The function T2EQ() implements the T^2-test for equivalence 
    according to Wellek (2010) <DOI:10.1201/ebk1439808184>.
    The function T2EQ.dissolution.profiles.hoffelder() implements a variant 
    of the T^2-test for equivalence according to Hoffelder (2016) 
    <http://www.ecv.de/suse_item.php?suseId=Z|pi|8430> for the 
    equivalence comparison of highly variable dissolution profiles.
	"""
	
	cran = "T2EQ" 

	version("1.1", md5="7c53dca51e8b8e10e3e24e48ad275a81")

