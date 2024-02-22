# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransplotr(RPackage):
	"""Visualize Transcript Structures in Elegant Way

	To visualize the gene structure with multiple isoforms better, I developed this package to draw different transcript structures easily.
	"""
	
	homepage = "https://github.com/junjunlab/transPlotR"
	cran = "transPlotR" 

	version("0.0.2", md5="0667a043a40b66e56a234b6a1cc2b9df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggarchery", type=("build", "run"))
	depends_on("r-geomtextpath", type=("build", "run"))
