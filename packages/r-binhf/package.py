# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinhf(RPackage):
	"""Haar-Fisz Functions for Binomial Data

	Binomial Haar-Fisz transforms for Gaussianization as in Nunes and Nason (2009).
	"""
	
	cran = "binhf" 

	version("1.0-3", md5="13442e5f0dc8d9a63ade26a113c329e6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-adlift@0.9.2:", type=("build", "run"))
	depends_on("r-ebayesthresh", type=("build", "run"))
