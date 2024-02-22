# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGear(RPackage):
	"""Geostatistical Analysis in R

	Implements common geostatistical methods in a clean, straightforward, efficient manner. The methods are discussed in Schabenberger and Gotway (2004, <ISBN:9781584883227>) and Waller and Gotway (2004, <ISBN:9780471387718>).
	"""
	
	cran = "gear" 

	version("0.3.4", md5="87a17cb1e28dbe2b4b8c62996876f795")

	depends_on("r-autoimage", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
