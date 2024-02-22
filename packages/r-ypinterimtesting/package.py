# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYpinterimtesting(RPackage):
	"""Interim Monitoring Using Adaptively Weighted Log-Rank Test in
Clinical Trials

	For any spending function specified by the user, this 
    package provides corresponding boundaries for interim testing using
    the adaptively weighted log-rank test developed by Yang and Prentice
    (2010 <doi:10.1111/j.1541-0420.2009.01243.x>). 
    The package uses a re-sampling method to obtain stopping boundaries 
    at the interim looks.The output consists of stopping boundaries 
    and observed values of the test statistics at the interim looks, 
    along with nominal p-values defined as the probability of the test 
    exceeding the specific observed test statistic value or critical 
    value, regardless of the test behavior at other looks. 
    The asymptotic validity of the stopping boundaries is established
    in Yang (2018 <doi:10.1002/sim.7958>).
	"""
	
	cran = "YPInterimTesting" 

	version("1.0.3", md5="c7d2c63cd1226e4d59467c84bb03de38")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
