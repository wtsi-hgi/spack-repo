# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendroanalyst(RPackage):
	"""A Tool for Processing and Analyzing Dendrometer Data

	There are various functions for managing and cleaning data before the application of different approaches. This includes identifying and erasing sudden jumps in dendrometer data not related to environmental change, identifying the time gaps of recordings, and changing the temporal resolution of data to different frequencies. Furthermore, the package calculates daily statistics of dendrometer data, including the daily amplitude of tree growth. Various approaches can be applied to separate radial growth from daily cyclic shrinkage and expansion due to uptake and loss of stem water. In addition, it identifies periods of consecutive days with user-defined climatic conditions in daily meteorological data, then check what trees are doing during that period. 
	"""
	
	cran = "dendRoAnalyst" 

	version("0.1.5", md5="4d78ba406296aef87b4a7a73b83ccdc8")
	version("0.1.4", md5="94bb809a972042318f4ddcea902dad5f")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
