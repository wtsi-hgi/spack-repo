# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR4googleads(RPackage):
	"""'Google Ads API' Interface

	Interface for the 'Google Ads API'. 'Google Ads' is an online
    advertising service that enables advertisers to display advertising to web
    users (see <https://developers.google.com/google-ads/> for more information).
	"""
	
	homepage = "https://github.com/banboo-data/r4googleads"
	cran = "r4googleads" 

	version("0.1.1", md5="15afc23b58a3f7a49806cb8346fa7f8e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
