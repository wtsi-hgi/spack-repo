# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInstagramadsr(RPackage):
	"""Access to Instagram Ads via the 'Windsor.ai' API

	Collect  marketing data from Instagram Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "instagramadsR" 

	version("0.1.0", md5="93bf9236bf2c8a1ca1f28c7a010ae2b4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
