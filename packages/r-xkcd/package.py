# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXkcd(RPackage):
	"""Plotting ggplot2 Graphics in an XKCD Style

	Plotting ggplot2 graphs using the XKCD style.
	"""
	
	cran = "xkcd" 

	version("0.0.6", md5="e76ef869d4a2fa3b12ada0ddc7482d9d")

	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
