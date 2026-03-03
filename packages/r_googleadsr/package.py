# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleadsr(RPackage):
	"""Access to 'Google Ads' via the 'Windsor.ai' API

	Collect  marketing data from 'Google Ads' using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	cran = "googleadsR" 

	version("1.0.0", md5="bb9098d2d6b435f1a4946d0bc9eeb9e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
