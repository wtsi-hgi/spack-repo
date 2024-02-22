# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleeperapi(RPackage):
	"""Wrapper Functions Around 'Sleeper' (Fantasy Sports) API

	For those wishing to interact with the 'Sleeper' (Fantasy Sports) API (<https://api.sleeper.app/>) without looking too much into its documentation (found at <https://docs.sleeper.app/>), this package offers wrapper functions around the available API calls to make it easier.
	"""
	
	cran = "sleeperapi" 

	version("1.0.4", md5="0219a44836748c4d34e21cac62563083")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
