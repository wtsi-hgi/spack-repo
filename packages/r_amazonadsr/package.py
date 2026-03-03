# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmazonadsr(RPackage):
	"""Get Amazon Ads Data via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from Amazon Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "amazonadsR" 

	version("0.1.0", md5="36762583b18809f889df8ecf4da8d80d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
