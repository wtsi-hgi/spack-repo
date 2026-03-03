# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkedinadsr(RPackage):
	"""Access to 'LinkedIn' Ads via the 'Windsor.ai' API

	Collect  marketing data from 'LinkedIn' Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "linkedInadsR" 

	version("0.1.0", md5="c69ce9568f6f30a066249968aaa6b42f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
