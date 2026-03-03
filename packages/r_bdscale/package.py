# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdscale(RPackage):
	"""Remove Weekends and Holidays from ggplot2 Axes

	Provides a continuous date scale, omitting weekends and holidays.
	"""
	
	homepage = "http://github.com/dvmlls/bdscale"
	cran = "bdscale" 

	version("2.0.0", md5="41eb6332dd3cf5b4a2c27c3478f2b383")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-scales@0.3:", type=("build", "run"))
