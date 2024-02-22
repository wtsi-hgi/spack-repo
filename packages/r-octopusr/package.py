# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROctopusr(RPackage):
	"""Interact with the 'Octopus Energy' API

	A simple wrapper for the 'Octopus Energy' API
    <https://developer.octopus.energy/docs/api/>. It handles
    authentication, by storing a provided API key and meter details.
    Implemented endpoints include 'products' for viewing tariff details
    and 'consumption' for viewing meter consumption data.
	"""
	
	homepage = "https://github.com/Moohan/octopusR"
	cran = "octopusR" 

	version("1.0.1", md5="8bcd064bb2a408b0d54adea5586a1b85")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
