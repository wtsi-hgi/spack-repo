# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROacolors(RPackage):
	"""OpenAnalytics Colors Package

	Provides carefully chosen color palettes as used a.o. at OpenAnalytics <http://www.openanalytics.eu>.
	"""
	
	homepage = "http://www.openanalytics.eu"
	cran = "oaColors" 

	version("0.0.4", md5="34d559c07e67f2f767ca99271c3f17d5")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
