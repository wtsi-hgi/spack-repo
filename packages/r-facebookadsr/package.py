# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFacebookadsr(RPackage):
	"""Access to Facebook Ads via the 'Windsor.ai' API

	Collect  marketing data from facebook Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
    Use four spaces when indenting paragraphs within the Description.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "facebookadsR" 

	version("0.1.0", md5="5c10ae9afa28484e40ab3cb2e261348e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
