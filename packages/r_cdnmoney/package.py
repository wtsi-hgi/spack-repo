# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdnmoney(RPackage):
	"""Components of Canadian Monetary and Credit Aggregates

	Components of Canadian Credit Aggregates and Monetary Aggregates with continuity adjustments.
	"""
	
	cran = "CDNmoney" 

	version("2012.4-2", md5="f128ad06f30024d01a8471587c40284d")

	depends_on("r@2.10:", type=("build", "run"))
