# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurkeyelections(RPackage):
	"""The Most Comprehensive R Package for Turkish Election Results

	Includes the results of general, local, and presidential elections held in Turkey between 1995 and 2023, broken down by provinces and overall national results. It facilitates easy processing of this data and the creation of visual representations based on these election results.
	"""
	
	homepage = "https://github.com/ozancanozdemir/turkeyelections"
	cran = "turkeyelections" 

	version("0.1.1", md5="24dbc783464ebc1a22a42bfcc2444ecb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggparliament", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
