# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncApi(RPackage):
	"""Oceans 2.0 API Client Library

	Allows users to discover and retrieve Ocean Networks Canada's oceanographic data in raw, text, image, audio, video or any other format available. Provides a class that wraps web service calls and business logic so that users can download data with a single line of code.
	"""
	
	homepage = "https://wiki.oceannetworks.ca/display/O2A/Oceans+2.0+API+Home"
	cran = "onc.api" 

	version("2.0.1.0", md5="937dd69e2b35ee7eb349ac236d3230b5")

	depends_on("r-anytime", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-humanize", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
