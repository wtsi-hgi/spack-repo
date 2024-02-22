# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCumulocityr(RPackage):
	"""Client for the 'Cumulocity' API

	Access the 'Cumulocity' API and retrieve data on devices, measurements, and events. Documentation for the API can be found at <https://www.cumulocity.com/guides/reference/rest-implementation/>.
	"""
	
	homepage = "https://softwareag.github.io/cumulocityr/"
	cran = "cumulocityr" 

	version("0.1.0", md5="98af8972656bbc020e016e126c657082")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
