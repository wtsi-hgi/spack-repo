# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXkcdcolors(RPackage):
	"""Color Names from the XKCD Color Survey

	The XKCD color survey asked participants to name colours. Randall Munroe published the top thousand(roughly) names and their sRGB hex values. This package lets you use them.
	"""
	
	cran = "xkcdcolors" 

	version("1.0", md5="3e15fa40d1e961f2be63ce9e53bd259a")

	depends_on("r-fnn", type=("build", "run"))
