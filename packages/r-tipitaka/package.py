# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipitaka(RPackage):
	"""Data and Tools for Analyzing the Pali Canon

	Provides access to the complete Pali Canon, or
    Tipitaka, the canonical scripture for Theravadin Buddhists 
    worldwide. Based on the Chattha Sangayana Tipitaka version
    4 (Vipassana Research Institute, 1990).
	"""
	
	cran = "tipitaka" 

	version("0.1.2", md5="f75941e0b1d163f96874b56df235ad8a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
