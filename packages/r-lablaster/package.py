# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLablaster(RPackage):
	"""Laser Ablation Blast Through Endpoint Detection

	Imports a data frame containing a single time resolved laser ablation mass spectrometry analysis of a foraminifera (or other carbonate shell), then detects when the laser has burnt through the foraminifera test as a function of change in signal over time.
	"""
	
	homepage = "https://github.com/alexsb1/lablaster"
	cran = "lablaster" 

	version("1.0.1", md5="378c60c4fb65a707c815a2565ddf901e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-smooth", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
