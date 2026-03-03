# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForcer(RPackage):
	"""Force Measurement Analyses

	For cleaning and analysis of graphs, such as animal closing force 
    measurements. 
    'forceR' was initially written and optimized to deal with insect bite force 
    measurements, but can be used for any time series. Includes a full workflow 
    to load, plot and crop data, correct amplifier and baseline drifts, 
    identify individual peak shapes (bites), rescale (normalize) peak curves, 
    and find best polynomial fits to describe and analyze force curve shapes.
	"""
	
	homepage = "https://github.com/Peter-T-Ruehr/forceR"
	cran = "forceR" 

	version("1.0.20", md5="02f6a70fc19dfd90096c3ca27988aec2")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-filesstrings", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-roll", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
