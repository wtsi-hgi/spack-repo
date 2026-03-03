# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalkscoreapi(RPackage):
	"""Walk Score and Transit Score API

	A collection of functions to perform the Application
        Programming Interface (API) calls associated with the Walk
        Score website (www.walkscore.com) within the R environment.
        These functions can be used to query the Walk Score and Transit
        Score database for a wide variety of information using R
        scripts. This package includes the simple Walk Score and
        Transit Score API calls, which return the scores associated
        with an input location, as well as calls which return some data
        used to calculate the scores. These functions are especially
        useful for mass data collection and gathering Walk Score and
        Transit Score values for large lists of locations.
	"""
	
	cran = "walkscoreAPI" 

	version("1.2", md5="dec373aa4bd7a8b2ee8ce37204fadccc")

