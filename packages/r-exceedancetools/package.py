# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExceedancetools(RPackage):
	"""Confidence/Credible Regions for Exceedance Sets and Contour
Lines

	Provides methods for constructing confidence or credible regions
    for exceedance sets and contour lines.
	"""
	
	cran = "ExceedanceTools" 

	version("1.3.6", md5="ffd645c9588a316150e2591e3b9e97f4")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-spatialtools", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
