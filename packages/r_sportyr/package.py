# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSportyr(RPackage):
	"""Plot Scaled 'ggplot' Representations of Sports Playing Surfaces

	Create scaled 'ggplot' representations of playing surfaces.
    Playing surfaces are drawn pursuant to rule-book specifications.
    This package should be used as a baseline plot for displaying any type of
    tracking data.
	"""
	
	homepage = "https://sportyr.sportsdataverse.org/"
	cran = "sportyR" 

	version("2.2.2", md5="b2e8904039c4711014d8150288c9ff39")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
