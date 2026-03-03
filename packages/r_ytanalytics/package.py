# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYtanalytics(RPackage):
	"""Wrapper for 'YouTube Analytics' API

	Simplify working with the 'YouTube Analytics' API <https://developers.google.com/youtube/analytics>. Collect traffic, 
    time period, location, and other data quickly and efficiently.
    For working with the 'YouTube Data' API, use the 'tuber' 'R' Package.
	"""
	
	cran = "YTAnalytics" 

	version("0.1.0", md5="290122e7c540502d1fa2b25f0eed2f43")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
