# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppleadsr(RPackage):
	"""Get Apple Search Ads Data via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from Apple Search Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "appleadsR" 

	version("0.1.0", md5="8e9b01ecdacd8f95a968e49e33f5f94c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
