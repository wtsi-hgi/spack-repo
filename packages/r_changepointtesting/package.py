# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointtesting(RPackage):
	"""Change Point Estimation for Clustered Signals

	A multiple testing procedure for clustered alternative hypotheses. 
    It is assumed that the p-values under the null hypotheses follow U(0,1) and 
    that the distributions of p-values from the alternative hypotheses are 
    stochastically smaller than U(0,1). By aggregating information, this 
    method is more sensitive to detecting signals of low magnitude than 
    standard methods. Additionally, sporadic small p-values appearing 
    within a null hypotheses sequence are avoided by averaging on the 
    neighboring p-values.
	"""
	
	cran = "ChangepointTesting" 

	version("1.1", md5="1d5d4aed43bb374b1a9b6d271e361e3b")

