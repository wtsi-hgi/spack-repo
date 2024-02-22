# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuoradsr(RPackage):
	"""Get 'Quora' Ads Data via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from 'Quora' Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "quoradsR" 

	version("0.1.0", md5="299fc1d47b4b24b120b7eca804e732dd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
