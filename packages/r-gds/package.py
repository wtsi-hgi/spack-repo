# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGds(RPackage):
	"""Descriptive Statistics of Grouped Data

	Contains a function called gds() which accepts three input
    parameters like lower limits, upper limits and the frequencies of the
    corresponding classes. The gds() function calculate and return the values
    of mean ('gmean'), median ('gmedian'), mode ('gmode'), variance ('gvar'), standard
    deviation ('gstdev'), coefficient of variance ('gcv'), quartiles ('gq1', 'gq2', 'gq3'),
    inter-quartile range ('gIQR'), skewness ('g1'), and kurtosis ('g2') which facilitate
    effective data analysis. For skewness and kurtosis calculations we use moments.
	"""
	
	cran = "gds" 

	version("0.1.1", md5="df2ca3e554f90b2551284770c59d29f1")

