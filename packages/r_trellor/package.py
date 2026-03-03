# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrellor(RPackage):
	"""Access the Trello API

	An R client for the Trello API. Supports free-tier features such as
    access to private boards, creating and updating cards and other resources,
    and downloading data in a structured way.
	"""
	
	homepage = "https://github.com/jchrom/trelloR"
	cran = "trelloR" 

	version("0.8.0", md5="dd3bfae732964e0954b2f16bdad9107a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
