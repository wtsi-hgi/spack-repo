# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbrads(RPackage):
	"""Analyzing and Managing Facebook Ads from R

	Wrapper functions around the Facebook Marketing 'API' to create,
    read, update and delete custom audiences, images, campaigns, ad sets, ads and
    related content.
	"""
	
	homepage = "https://github.com/daroczig/fbRads"
	cran = "fbRads" 

	version("17.0.0", md5="5554714015dd867e8ce238dde5c7d68d")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
