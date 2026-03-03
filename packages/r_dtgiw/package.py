# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtgiw(RPackage):
	"""Discrete Transmuted Generalized Inverse Weibull Distribution

	The Discrete Transmuted Generalized Inverse Weibull (DTGIW) distribution is a new distribution for count data analysis. The DTGIW is discrete distribution based on Atchanut and Sirinapa (2021). <DOI: 10.14456/sjst-psu.2021.149>.
	"""
	
	cran = "dtgiw" 

	version("1.0.0", md5="1c363270095363be49b6175a4fb2c5c2")

