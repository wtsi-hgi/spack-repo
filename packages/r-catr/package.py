# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatr(RPackage):
	"""Generation of IRT Response Patterns under Computerized Adaptive
Testing

	Provides routines for the generation of response patterns under unidimensional dichotomous and polytomous computerized adaptive testing (CAT) framework. It holds many standard functions to estimate ability, select the first item(s) to administer and optimally select the next item, as well as several stopping rules. Options to control for item exposure and content balancing are also available (Magis and Barrada (2017) <doi:10.18637/jss.v076.c01>).
	"""
	
	cran = "catR" 

	version("3.17", md5="f701904756d6122fa67a57e715c4ecd4")

	depends_on("r@4:", type=("build", "run"))
