# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigirhythm(RPackage):
	"""Analyzing Animal's Rhythmicity

	Analyze and visualize the rhythmic behavior of animals using the 
  degree of functional coupling (See Scheibe (1999) <doi:10.1076/brhm.30.2.216.1420>),
  compute and visualize harmonic power, actograms, average activity and diurnality 
  index.
	"""
	
	cran = "digiRhythm" 

	version("1.1", md5="0cc92122b6707d8e73b744c1d886103c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr@2.0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
