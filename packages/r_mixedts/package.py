# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedts(RPackage):
	"""Mixed Tempered Stable Distribution

	We provide detailed functions for univariate Mixed Tempered Stable distribution. 
	"""
	
	cran = "MixedTS" 

	version("1.0.4", md5="e85e18f4031c7f5964628ce964a7d2e3")

	depends_on("r-mass", type=("build", "run"))
