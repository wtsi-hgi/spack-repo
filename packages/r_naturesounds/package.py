# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaturesounds(RPackage):
	"""Animal Sounds for Bioacustic Analysis

	Collection of example animal sounds for bioacoustic analysis.
	"""
	
	homepage = "https://github.com/maRce10/NatureSounds"
	cran = "NatureSounds" 

	version("1.0.4", md5="6eb06774739ac1c5e70377175716beb8")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
