# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparsurv(RPackage):
	"""Nonparametric Tests for Main Effects, Simple Effects and
Interaction Effect in a Factorial Design with Censored Data

	Nonparametric Tests for Main Effects, Simple Effects and Interaction Effect with Censored Data and Two Factorial Influencing Variables.
	"""
	
	cran = "nparsurv" 

	version("0.1.0", md5="a54e87875e5bfd0df4a71ce02f05c37f")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-survival@2.38.3:", type=("build", "run"))
	depends_on("r-th-data@1.0.7:", type=("build", "run"))
