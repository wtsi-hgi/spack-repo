# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactor256(RPackage):
	"""Use Raw Vectors to Minimize Memory Consumption of Factors

	Uses raw vectors to minimize memory consumption of categorical 
    variables with fewer than 256 unique values. Useful for analysis of large
    datasets involving variables such as age, years, states, countries, or
    education levels.
	"""
	
	cran = "factor256" 

	version("0.1.0", md5="a27f04fcbfe765a0da27a0dfcb12be03", url="https://cran.r-project.org/src/contrib/factor256_0.1.0.tar.gz")

