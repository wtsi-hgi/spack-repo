# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccSampleSize(RPackage):
	"""Calculation of Sample Size and Power for ICC

	Provides functions to calculate the requisite sample size for studies where ICC is 
    the primary outcome. Can also be used for calculation of power. In both cases it
    allows the user to test the impact of changing input variables by calculating the outcome
    for several different values of input variables. Based off the work of Zou.
    Zou, G. Y. (2012). Sample size formulas for estimating intraclass correlation coefficients with
    precision and assurance. Statistics in medicine, 31(29), 3972-3981.
	"""
	
	cran = "ICC.Sample.Size" 

	version("1.0", md5="3ff7f060631c7a8174fb1ba72779bad6")

