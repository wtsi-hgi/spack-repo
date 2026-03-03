# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgalignment(RPackage):
	"""Plots 'D&D'-Style Alignment Charts

	'D&D' alignment charts show 9 boxes with values for good
    through evil and values for chaotic through lawful. This package
    easily creates these alignment charts from user-provided image paths
    and alignment values.
	"""
	
	cran = "ggalignment" 

	version("1.0.1", md5="aab873f4ff7b5a2c24857740fd040a56")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggimage@0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-magrittr@1:", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
