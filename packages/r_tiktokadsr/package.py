# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiktokadsr(RPackage):
	"""Access to TikTok Ads via the 'Windsor.ai' API

	Collect  marketing data from TikTok Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "tiktokadsR" 

	version("0.1.0", md5="fa4b0b92873754b230b51c6393bae6c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
