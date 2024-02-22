# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgisotonic(RPackage):
	"""'ggplot2' Friendly Isotonic or Monotonic Regression Curves

	Provides stat_isotonic() to add weighted univariate isotonic regression curves.
	"""
	
	homepage = "https://github.com/talegari/ggisotonic"
	cran = "ggisotonic" 

	version("0.1.2", md5="8af128cd5cf2113b9b3c167ccf5112d5")

	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.17:", type=("build", "run"))
