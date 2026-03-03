# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMediacloudr(RPackage):
	"""Wrapper for the 'mediacloud.org' API

	API wrapper to gather news stories, media information and tags from the 'mediacloud.org' API, based on a multilevel query <https://mediacloud.org/>. A personal API key is required.
	"""
	
	cran = "mediacloudr" 

	version("0.1.0", md5="9c1c4c360cbbb9f6a04c4ec2e6c8447a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
