# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNasadata(RPackage):
	"""Interface to Various NASA API's

	Provides functions to access NASA's Earth Imagery and Assets API
    and the Earth Observatory Natural Event Tracker (EONET) webservice.
	"""
	
	cran = "nasadata" 

	version("0.9.0", md5="4422260099ab6cff77afc1bcea18d669")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
