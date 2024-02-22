# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgcharts(RPackage):
	"""Shorten the Distance from Data Visualization Idea to Actual Plot

	Streamline the creation of common charts by taking care of a lot of
    data preprocessing and plot customization for the user. Provides a
    high-level interface to create plots using 'ggplot2'.
	"""
	
	homepage = "https://github.com/thomas-neitmann/ggcharts"
	cran = "ggcharts" 

	version("0.2.1", md5="8f0e39ad10ab0d121ef62dc1060ab453")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
