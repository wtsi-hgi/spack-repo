# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMccr(RPackage):
	"""The Matthews Correlation Coefficient

	The Matthews correlation coefficient (MCC) score is calculated (Matthews BW  (1975) <DOI:10.1016/0005-2795(75)90109-9>).
	"""
	
	cran = "mccr" 

	version("0.4.4", md5="a6ddb76aa886511378c5ef8209ea0b1b")

