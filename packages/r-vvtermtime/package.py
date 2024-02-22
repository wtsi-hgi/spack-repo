# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvtermtime(RPackage):
	"""Interface for 'Semestry TermTime' Services

	Provides an R interface for interacting with the 'Semestry TermTime' services.
    It allows users to retrieve scheduling data from the API. see
    <https://github.com/vusaverse/vvtermtime/blob/main/openapi_7.7.0.pdf> for details.
	"""
	
	homepage = "https://github.com/vusaverse/vvtermtime"
	cran = "vvtermtime" 

	version("0.0.1", md5="41fe0a2a02503ebcef367d51ae955cd2")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
