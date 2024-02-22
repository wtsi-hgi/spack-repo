# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhtdiscrete(RPackage):
	"""Multiple Hypotheses Testing for Discrete Data

	A comprehensive tool for almost all existing multiple testing
    methods for discrete data. The package also provides some novel multiple testing
    procedures controlling FWER/FDR for discrete data. Given discrete p-values
    and their domains, the [method].p.adjust function returns adjusted p-values,
    which can be used to compare with the nominal significant level alpha and make
    decisions. For users' convenience, the functions also provide the output option 
    for printing decision rules.
	"""
	
	homepage = "https://allen.shinyapps.io/MTPs/"
	cran = "MHTdiscrete" 

	version("1.0.1", md5="98e39e7d004a28f74bc25b2b5aa628c3")

