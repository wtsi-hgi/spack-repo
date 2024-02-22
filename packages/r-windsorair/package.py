# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWindsorair(RPackage):
	"""Access the 'Windsor.ai' API

	Collect multichannel marketing data from sources such as Google analytics, Facebook Ads, and many others using the 'Windsor.ai' API <https://www.windsor.ai/api-fields/>.
	"""
	
	homepage = "https://github.com/windsor-ai/windsoraiR/"
	cran = "windsoraiR" 

	version("0.1.2", md5="6e6f739987bf71ff339d160d3a888539")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
